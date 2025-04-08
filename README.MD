# 🎫 Get API Zendesk - Consulta de Tickets via Python

Este projeto é um script em Python que realiza **requisições à API do Zendesk** para buscar e exibir informações detalhadas de um ticket específico. Ideal para integrações com sistemas internos ou análises automatizadas de chamados.

---

## 🚀 Funcionalidades

- Conecta-se com a API do Zendesk utilizando autenticação via token.
- Busca um ticket específico por ID.
- Filtra e exibe os principais dados do ticket:
  - ID, Status, Prioridade, Assunto, Descrição
  - Datas de criação e atualização
  - Responsável, Solicitante
  - Tags e campos personalizados (CPF e Nome do Cliente)

---

## ⚙️ Pré-requisitos

- Conta Zendesk com token de API ativo
- Python 3.8 ou superior
- Biblioteca `dotenv` para leitura de variáveis de ambiente
- Certificado `certifi` para conexão HTTPS segura

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/Robalves-5/Get-API-Zendesk.git
cd Get-API-Zendesk


├── Requisicao.py                         
├── requeriments.txt      
├── .gitignore            
└── README.md  


===== Detalhes do Ticket Zendesk =====
ID: 101
Criado em: 2024-10-01T12:00:00Z
Status: open
Prioridade: high
Assunto: Erro no sistema
...




