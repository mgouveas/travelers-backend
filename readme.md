# Backend para Aplicativo de Gestão de Viagens

Bem-vindo ao repositório do backend para o nosso aplicativo de gestão de viagens! Este projeto fornece a API e a lógica de negócios necessárias para gerenciar e organizar suas viagens de maneira eficiente.

## Descrição

Este repositório contém o código-fonte para o backend do nosso aplicativo de gestão de viagens, desenvolvido em Python. O sistema é projetado para ajudar os usuários a planejar, monitorar e gerenciar suas viagens, oferecendo funcionalidades robustas e escaláveis. A API expõe uma série de endpoints que permitem aos usuários criar, consultar e atualizar informações sobre destinos, itinerários e reservas.

## Funcionalidades

- **Gerenciamento de Destinos:** Adicione, edite e remova destinos de viagem.
- **Planejamento de Itinerários:** Crie e modifique itinerários detalhados para suas viagens.
- **Reservas:** Faça e gerencie reservas de voos, hotéis e transporte.
- **Usuários e Autenticação:** Gerencie contas de usuário com autenticação e autorização seguras.
- **Relatórios e Análises:** Gere relatórios sobre suas viagens e obtenha análises úteis.

## Tecnologias

- **Linguagem:** Python 3.x
- **Framework:** FastAPI (para criação de APIs rápidas e eficientes)
- **Banco de Dados:** PostgreSQL (para armazenamento de dados relacionais)
- **ORM:** SQLAlchemy (para interações com o banco de dados)
- **Autenticação:** OAuth 2.0 / JWT (para segurança e gestão de sessões)
- **Documentação:** Swagger (integrado com FastAPI para documentação interativa)

## Estrutura do Projeto

- **app/**: Contém o código principal da aplicação.
  - **api/**: Definição dos endpoints e roteamento.
  - **models/**: Modelos de dados e definições de banco de dados.
  - **services/**: Lógica de negócios e serviços.
  - **utils/**: Funções utilitárias e helpers.
- **tests/**: Testes automatizados para garantir a qualidade do código.
- **migrations/**: Scripts de migração de banco de dados.
- **config/**: Arquivos de configuração e variáveis de ambiente.

## Configuração e Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
    
4. Configure o banco de dados e as variáveis de ambiente:

    * Copie o arquivo .env.example para .env e ajuste as variáveis conforme necessário.

5. Aplique as migrações:
    ```bash
    alembic upgrade head
    ```

6. Inicie o servidor:
    ```bash
    uvicorn app.main:app --reload
    ```

## Contribuindo

Estamos abertos a contribuições! Se você deseja ajudar a melhorar este projeto, por favor, siga estas etapas:

1. Fork o repositório.
2. Crie uma branch para a sua feature (git checkout -b minha-nova-feature).
3. Faça suas alterações e commit (git commit -am 'Adiciona nova feature').
4. Envie para o repositório remoto (git push origin minha-nova-feature).
5. Crie um pull request.


## Licença
Este projeto está licenciado sob a _Licença MIT_.

Contato
Para mais informações ou suporte, entre em contato com a equipe de desenvolvimento através do e-mail: suporte@seusite.com.

___
<br>

# APLICAÇÃO

## Regras de Negócio

* O usuário cadastra uma viagem informando o local de destino, data de ínicio, data de término, e-mails dos convidados e também seu nome completo e endereço de e-mail;
* O criados  da viagem recebe um e-mail para confirmar a nova viagem através de um link. Ao clicar no link, a viagem é confirmada, os convidados recebem um e-mail de confirmação de presença e o criador é redirecionado para a página da viagem;
* Os convidados, ao clicarem no link de confirmação de presença, são direcionados para a aplicação onde devem inserir seu nome (além do e-mail que já estará preenchido) e então estarão confirmados na viagem;
* Na página do evento, o criador e os convidados podem adicionar links importantes da viagem como reserva do AirBnB, locais para serem visitados, etc...
* Ainda na página do evento, o criador e os convidados podem adicionar atividades que irão ocorrer durante a viagem com título, data e horário;
* Novos participantes podem ser convidados dentro da página do evento através do e-mail e assim devem passar pelo fluxo de confirmação como qualquer outro convidado;