from app.core.database import SessionLocal
from app.models.faq_model import PerguntaFAQ

def popular_banco():
    # Abre a ligação com a base de dados
    db = SessionLocal()

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

    adicionadas = 0

    for item in perguntas_iniciais:
        # Verifica se a pergunta já existe para não duplicar
        existe = db.query(PerguntaFAQ).filter(PerguntaFAQ.pergunta == item["pergunta"]).first()

        if not existe:
            nova_faq = PerguntaFAQ(
                pergunta=item["pergunta"],
                resposta=item["resposta"],
                categoria=item["categoria"]
            )
            db.add(nova_faq)
            adicionadas += 1
            print(f"Adicionada: {item['pergunta']}")

    db.commit()
    db.close()

    print(f"\nSucesso! {adicionadas} novas perguntas foram inseridas na base de dados.")

if __name__ == "__main__":
    popular_banco()