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
    },
    {
        "pergunta": "Quais são as formas de pagamento aceitas?",
        "resposta": "Aceitamos cartões de crédito (Visa, Mastercard, Elo, Amex), cartões de débito e pagamento via PIX.",
        "categoria": "Financeiro"
    },
    {
        "pergunta": "Esqueci a minha senha, como posso recuperá-la?",
        "resposta": "Na tela de login, clique em 'Esqueci minha senha'. Enviaremos um e-mail com as instruções para você criar um novo acesso de forma segura.",
        "categoria": "Conta"
    },
    {
        "pergunta": "Posso baixar filmes e séries para assistir offline?",
        "resposta": "Sim! No aplicativo para celulares e tablets, clique no ícone de download ao lado do episódio desejado. O título ficará salvo na aba 'Downloads'.",
        "categoria": "Conteúdo"
    },
    {
        "pergunta": "O aplicativo fecha sozinho durante a reprodução. O que fazer?",
        "resposta": "Verifique se o aplicativo está atualizado na loja do seu dispositivo. Recomendamos também limpar o cache ou, se necessário, reinstalar o aplicativo.",
        "categoria": "Suporte Técnico"
    },
    {
        "pergunta": "Consigo assistir à programação ao vivo?",
        "resposta": "Sim, você pode acompanhar a transmissão ao vivo dos canais disponíveis no seu plano acessando a seção 'Ao Vivo' no menu principal.",
        "categoria": "Conteúdo"
    },
    {
        "pergunta": "Como mudar o idioma do áudio ou ativar as legendas?",
        "resposta": "Durante a reprodução do vídeo, clique no ícone de engrenagem ou de balão de diálogo no canto da tela para escolher as opções de áudio e legenda desejadas.",
        "categoria": "Suporte Técnico"
    },
    {
        "pergunta": "Como faço para excluir o meu perfil secundário?",
        "resposta": "Acesse as configurações da sua conta, clique em 'Gerenciar Perfis', selecione o perfil que deseja remover e confirme clicando no botão 'Excluir perfil'.",
        "categoria": "Conta"
    },
    {
        "pergunta": "A minha fatura foi cobrada em duplicidade, como resolvo?",
        "resposta": "Caso identifique uma cobrança duplicada, acesse o painel 'Pagamentos' e clique em 'Contestar cobrança', ou acione um dos nossos atendentes humanos no chat para realizarmos o estorno.",
        "categoria": "Financeiro"
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