# ---------------------------------------------------
# Script para popular a base de dados em Produção
# Criado por R.P.
# ---------------------------------------------------
import requests

# A URL oficial da sua API no Render
BASE_URL = "https://chatbot-v8a5.onrender.com/api/v1/chatbot/adicionar"

perguntas_iniciais = [
    {
        "pergunta": "Como alterar a forma de pagamento?",
        "resposta": "Aceda a 'Minha Conta' > 'Pagamentos' e clique em 'Editar forma de pagamento' para inserir o seu novo cartão de crédito.",
        "categoria": "Financeiro"
    },
    {
        "pergunta": "Como cancelar a minha assinatura?",
        "resposta": "Para cancelar, vá a 'Minha Assinatura', deslize até ao final da página e clique no botão vermelho 'Cancelar plano'.",
        "categoria": "Financeiro"
    },
    {
        "pergunta": "O vídeo está a travar muito, o que faço?",
        "resposta": "Recomendamos que verifique a sua ligação à internet. Se o problema persistir, limpe o cache do seu navegador ou reinicie a sua box.",
        "categoria": "Suporte Técnico"
    },
    {
        "pergunta": "Em quais dispositivos posso assistir?",
        "resposta": "Pode assistir no seu smartphone, tablet, computador e nas principais Smart TVs do mercado através do nosso aplicativo oficial.",
        "categoria": "Suporte Técnico"
    },
    {
        "pergunta": "Como alterar o meu e-mail de registo?",
        "resposta": "No painel de utilizador, clique em 'Perfil' > 'Dados pessoais' e edite o campo de e-mail. Receberá um link de confirmação no novo endereço.",
        "categoria": "Conta"
    },
    {
        "pergunta": "Quantas pessoas podem usar a minha conta ao mesmo tempo?",
        "resposta": "O plano padrão permite até 3 ecrãs em simultâneo. Pode atualizar o seu plano a qualquer momento para ter mais ecrãs.",
        "categoria": "Conta"
    }
]

def enviar_dados():
    adicionadas = 0
    print("A iniciar o envio de dados para o Render...\n")

    for item in perguntas_iniciais:
        try:
            # Nota: verify=False utilizado temporariamente para contornar bloqueio de certificado SSL local no Windows.
            response = requests.post(BASE_URL, json=item, verify=False)

            if response.status_code == 200:
                resultado = response.json()
                if resultado.get("status") == "sucesso":
                    print(f"✅ Adicionada: {item['pergunta']}")
                    adicionadas += 1
                else:
                    print(f"⚠️ Ignorada (já existe): {item['pergunta']}")
            else:
                print(f"❌ Erro {response.status_code} ao enviar: {item['pergunta']}")

        except Exception as e:
            print(f"❌ Falha de conexão na pergunta '{item['pergunta']}': {e}")

    print(f"\nConcluído! {adicionadas} novas perguntas foram registadas na nuvem.")

if __name__ == "__main__":
    enviar_dados()