import requests

# URL da nova rota de limpeza no Render
URL = "https://chatbot-v8a5.onrender.com/api/v1/chatbot/limpar-banco"

# Fazemos um DELETE com verify=False igual fizemos no POST
response = requests.delete(URL, verify=False)

if response.status_code == 200:
    print("✅ Sucesso:", response.json())
else:
    print("❌ Erro:", response.status_code, response.text)