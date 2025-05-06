import os
from decouple import config

from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import HuggingFaceEmbeddings


os.environ['GROQ_API_KEY'] = config('GROQ_API_KEY')

class AiBot:

    def __init__(self):
        self.__chat = ChatGroq(model='llama-3.3-70b-versatile')
        self.__retriever = self.__build_retriever()

    def __build_retriever(self):
        persist_directory = '/app/chroma_data'
        embedding = HuggingFaceEmbeddings()

        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding
        )

        return vector_store.as_retriever(
            search_kwargs={'k': 30},
        )
    
    def __build_messages(self, history_messages, question):
        messages = []
        for message in history_messages:
            message_class = HumanMessage if message.get('fromMe') else AIMessage
            messages.append(message_class(content=message.get('body')))
        messages.append(HumanMessage(content=question))
        return messages
    
    def invoke(self, history_messages, question):
        SYSTEM_TEMPLATE = '''
        Responda as perguntas dos usuários com base no contexto abaixo.
        Você é um assistente especializado em tirar dúvidas sobre Estratégias de Crescimento Sustentável em Pequenas e 
        Médias Empresas.
        Tire dúvidas dos possíveis usuários que entrarem em contato.
        Responda de forma natural, agradável e respeitosa. Seja objetivo nas respostas, com informações claras e diretas.
        Foque em ser natural e humanizado, como um diálogo comum entre duas pessoas. Leve em consideração também o histórico de
        mensagens da conversa com o usuário.
        Responsa sempre em português brasileiro.

        <context>
        {context}
        </context>
        '''

        docs = self.__retriever.invoke(question)
        question_answering_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    SYSTEM_TEMPLATE
                ),
                MessagesPlaceholder(variable_name='messages'),
            ]
        )
        document_chain = create_stuff_documents_chain(self.__chat, question_answering_prompt)
        response = document_chain.invoke(
            {
                'context': docs,
                'messages': self.__build_messages(history_messages, question),
            }
        )
        return response


    # MÉTODO USADO PARA PERSONALIZAR RESPOSTA GENERICA DO GROQ
    # def invoke(self, question):
    #         prompt = PromptTemplate(
    #             input_variables=['texto'],
    #             template='''
    #             Você é um especialista em todos os assuntos.
    #             Responda sempre utilizando dados detalhados e uma linguagem simples.
    #             Use emoji sempre que possível
    #             <texto>
    #             {texto}
    #             </texto>
    #             '''
    #         )
    #         chain = prompt | self.__chat | StrOutputParser()
    #         response = chain.invoke({
    #             'texto': question,
    #         })
    #         return response