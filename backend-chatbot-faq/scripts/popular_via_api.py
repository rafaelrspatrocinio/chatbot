import urllib.request
import json

def popular_api():
    # O endereço da sua API que está a correr no Docker
    url = 'http://localhost:8000/api/v1/faq/'

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

    sucessos = 0

    for item in perguntas_iniciais:
        # Prepara a requisição POST para o FastAPI
        dados = json.dumps(item).encode('utf-8')
        req = urllib.request.Request(
            url,
            data=dados,
            headers={'Content-Type': 'application/json', 'Accept': 'application/json'},
            method='POST'
        )

        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200 or response.status == 201:
                    sucessos += 1
                    print(f"Sucesso: '{item['pergunta']}' inserida na API!")
        except Exception as e:
            print(f"Aviso: Não foi possível inserir '{item['pergunta']}'. Motivo: {e}")

    print(f"\nFinalizado! {sucessos} perguntas cadastradas no Docker.")

if __name__ == "__main__":
    popular_api()