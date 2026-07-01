# Desafio Full Stack 02 – Chatbot de FAQ com Dashboard Analítico

Este projeto é uma solução Full Stack desenvolvida para automatizar o atendimento de dúvidas recorrentes e fornecer informações estratégicas sobre o comportamento dos utilizadores através de um painel analítico interativo.

## 🚀 Tecnologias Utilizadas

O projeto foi construído com uma arquitetura moderna, separando completamente as responsabilidades de interface (Frontend) e regras de negócio (Backend).

**Frontend (Interface do Utilizador):**
- **ReactJS** (com **Vite** para alta performance)
- **Axios** (para consumo da API REST)
- **Recharts** (para renderização dos gráficos analíticos)
- **Lucide-React** (biblioteca de ícones vetorizados)

**Backend (Motor e API):**
- **Python 3**
- **FastAPI** (alta performance e documentação Swagger nativa)
- **SQLAlchemy** (ORM para gestão da base de dados)
- **SQLite** (banco de dados leve para desenvolvimento)

**Infraestrutura:**
- **Docker** (para conteinerização e isolamento do ambiente Backend)

---

## 📁 Estrutura do Projeto

O código está organizado em dois diretórios independentes para garantir o desacoplamento:

```text
/
├── backend-chatbot-faq/   # Contém a API REST, banco de dados e arquivos do Docker
└── frontend-chatbot/      # Contém a interface em React e o Dashboard