
# Whatsapp chatbot com inteligencia artificial

Chatbot simples para whatsapp utilizando Waha Whatsapp API, Flask e Groq.

## Pré-requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes softwares instalados:

* [Docker](https://www.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Groq Api Key](https://console.groq.com)

## Configuração

1.  **Clone o repositório:**

    ```bash
    git clone git@github.com:maindan/chatbot.git
    ```

2.  **Construa e execute o container Docker:**

    Abra o terminal na pasta principal do projeto e rode o comando:
    ```bash
    docker-compose up --build
    ```
    Aguarde até que a aplicação esteja operante, leva alguns instantes até que a aplicação conclua a inicialização

3.  **Acesse a aplicação:**

    * Waha dashboard: `http://localhost:3000/dashboard`
    * Waha endpoints: `http://localhost:3000`
    * Backend: `http://localhost:5000`

    Acesse: 
    ```bash
    http://localhost:3000/dashboard
    ```
    para acessar o dashboard do waha e conectar ao seu whatsapp, configure o webhook da sessão para
    ```bash
    http://api:5000/chatbot/webhook
    ``` 
    e todas as mensagem serão encaminhadas para a api.

    Esta apenas mostr
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`GROQ_API_KEY`


## Stack utilizada
**Whatsapp:** Waha: https://waha.devlike.pro/ \
**Back-end:** Flask, Langchain e Requests para services \
**Virtualização:** Docker, Docker Compose \
**LLM:** GroqCloud: https://console.groq.com/home

## Melhorias
Este código possui uma implementação básica de LLM para responder a perguntas feitas ao número logado, a implementação de uma RAG junto ao conjunto da aplicação é essencial para dar um contexto a aplicação e personalizar o modelo de linguagem para interagir de forma mais natural e atender a demandas específicas.
O tutorial para implementação de RAG no chatbot pode ser encontrado em: https://www.youtube.com/watch?v=NQ6zNXX4qCo&ab_channel=PycodeBR

O arquivo com instruções de resposta do chatbot está em: `bot/ai_bot.py`
