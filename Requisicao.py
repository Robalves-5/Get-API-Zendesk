import http.client
import ssl
import certifi
import json
from base64 import b64encode
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
dotenv_path_env = r'C:\Users\robson.alves\Documents\Credenciais-zendesk\.env'
load_dotenv(dotenv_path=dotenv_path_env)

# Informações básicas
subdomain = 'genialhelp'
email = os.getenv("ZENDESK_EMAIL")
api_token = os.getenv("ZENDESK_API_TOKEN")

# ID do ticket desejado
ticket_id = 101
url_path = f"/api/v2/tickets/{ticket_id}.json"
full_url = f"https://{subdomain}.zendesk.com{url_path}"
print(f"Fazendo requisição para: {full_url}")

# Contexto SSL seguro com verificação de certificado
context = ssl.create_default_context()
context.load_verify_locations(cafile=certifi.where())

# Conexão HTTPS com o Zendesk
conn = http.client.HTTPSConnection(f"{subdomain}.zendesk.com", context=context)

# Cabeçalho de autenticação
auth_value = f"{email}/token:{api_token}"
encoded_auth = b64encode(auth_value.encode("utf-8")).decode("utf-8")

headers = {
    "Authorization": f"Basic {encoded_auth}"
}

# Enviar requisição
conn.request("GET", url_path, headers=headers)

# Obter resposta
response = conn.getresponse()

if response.status == 200:
    data = json.loads(response.read().decode())
    ticket = data.get("ticket", {})

    # Filtrar campos relevantes
    filtered_data = {
        "ID": ticket.get("id"),
        "Criado em": ticket.get("created_at"),
        "Atualizado em": ticket.get("updated_at"),
        "Status": ticket.get("status"),
        "Prioridade": ticket.get("priority"),
        "Assunto": ticket.get("subject"),
        "Descrição": ticket.get("description"),
        "Solicitante ID": ticket.get("requester_id"),
        "Responsável ID": ticket.get("assignee_id"),
        "Tags": ticket.get("tags"),
        "Nome do Cliente": next((field["value"] for field in ticket.get("custom_fields", []) if field["id"] == 360016955172), "Não informado"),
        "CPF": next((field["value"] for field in ticket.get("custom_fields", []) if field["id"] == 360016986131), "Não informado"),
    }

    # Exibir os dados do ticket
    print("\n===== Detalhes do Ticket Zendesk =====")
    for key, value in filtered_data.items():
        print(f"{key}: {value}")

else:
    print(f"Erro ao acessar a API. Status Code: {response.status}")

# Fechar conexão
conn.close()
