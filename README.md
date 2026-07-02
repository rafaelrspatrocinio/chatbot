# Desafio Full Stack 02 – Chatbot de FAQ com Dashboard Analítico

Este projeto é uma solução Full Stack desenvolvida para automatizar o atendimento de dúvidas recorrentes, fornecendo suporte técnico/administrativo em tempo real e mantendo a persistência de dados em ambiente de nuvem.

## 🔗 Links Oficiais
* **Aplicação em Produção:** [Assistente Virtual Globo](https://chatbot-theta-inky-41.vercel.app/)
* **Repositório do Código:** [GitHub - rafaelrspatrocinio/chatbot](https://github.com/rafaelrspatrocinio/chatbot)

---

## 🚀 Tecnologias Utilizadas

O projeto foi construído com uma arquitetura moderna e escalável, utilizando serviços em nuvem para garantir alta disponibilidade.

**Frontend (Interface do Usuário):**
- **ReactJS** (com **Vite** para alta performance)
- **Axios** (para consumo da API REST)
- **Lucide-React** (ícones vetorizados)
- **Hospedagem:** Vercel

**Backend (Motor e API):**
- **Python 3**
- **FastAPI** (alta performance e documentação Swagger nativa)
- **SQLAlchemy** (ORM para gestão da base de dados)
- **PostgreSQL** (Banco de dados relacional hospedado na nuvem via Render)

**Infraestrutura:**
- **Render:** Hospedagem do serviço de backend e Banco de Dados (PostgreSQL).
- **Docker:** Utilizado para conteinerização e isolamento do ambiente.

---

📊 Catálogo de Conhecimento
O sistema utiliza um motor de busca inteligente que identifica termos nas perguntas ou nas categorias abaixo para retornar a resposta correspondente.

Categoria: Financeiro
Pergunta: Quais são as formas de pagamento aceitas?

Resposta: Aceitamos cartões de crédito (Visa, Mastercard, Elo, Amex), cartões de débito e pagamento via PIX.

Pergunta: Como faço para mudar ou fazer upgrade no meu plano?

Resposta: Vá até 'Minha Conta', selecione 'Minha Assinatura' e clique em 'Alterar plano'.

Pergunta: A minha fatura foi cobrada em duplicidade?

Resposta: Acesse o painel 'Pagamentos' e clique em 'Contestar cobrança', ou acione um atendente.

Categoria: Conta
Pergunta: Esqueci a minha senha, como posso recuperá-la?

Resposta: Na tela de login, clique em 'Esqueci minha senha'. Enviaremos um e-mail com as instruções.

Pergunta: Como criar um perfil infantil (Kids)?

Resposta: Acesse 'Gerenciar Perfis', clique em 'Adicionar Perfil' e ative a opção 'Perfil Infantil'.

Pergunta: Como faço para excluir o meu perfil secundário?

Resposta: Acesse 'Gerenciar Perfis', selecione o perfil que deseja remover e clique em 'Excluir perfil'.

Categoria: Conteúdo
Pergunta: Posso baixar filmes e séries para assistir offline?

Resposta: Sim! No app mobile, clique no ícone de download ao lado do episódio desejado.

Pergunta: Consigo assistir à programação ao vivo?

Resposta: Sim, acesse a seção 'Ao Vivo' no menu principal para acompanhar os canais disponíveis.

Pergunta: Como faço para assistir aos jogos do Flamengo ao vivo?

Resposta: Verifique se o seu plano inclui o pacote Premiere ou acesse a transmissão via SporTV e TV aberta.

Pergunta: Por quanto tempo os downloads ficam disponíveis offline?

Resposta: Títulos baixados permanecem salvos por até 30 dias (ou 48h após o início da reprodução).

Categoria: Suporte Técnico
Pergunta: O aplicativo fecha sozinho durante a reprodução. O que fazer?

Resposta: Verifique atualizações, limpe o cache do dispositivo ou reinstale o aplicativo.

Pergunta: Como mudar o idioma do áudio ou ativar as legendas?

Resposta: Durante a reprodução, clique no ícone de engrenagem ou balão de diálogo.

Pergunta: Minha Smart TV não tem o aplicativo, o que fazer?

Resposta: Utilize dispositivos como Chromecast, Apple TV ou Roku Express na entrada HDMI.

## 📁 Estrutura do Projeto

```text
/
├── backend-chatbot-faq/   # API REST, modelos SQLAlchemy e scripts de deploy
└── frontend-chatbot/      # Interface React, lógica de chat e consumo da API


