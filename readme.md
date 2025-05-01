
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
    git clone git@github.com:maindan/desafio-fpf.git
    ```

2.  **Construa e execute os containers Docker:**

    Abra o terminal na pasta principal do projeto e rode o comando:
    ```bash
    docker-compose up --build
    ```
    Aguarde até que a aplicação esteja operante, leva alguns minutos até que a aplicação conclua a inicialização

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