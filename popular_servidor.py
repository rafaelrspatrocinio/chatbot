# ---------------------------------------------------
# Script para popular a base de dados em Produção
# Criado por R.P.
# ---------------------------------------------------
import requests

# A URL oficial da sua API no Render
BASE_URL = "https://chatbot-v8a5.onrender.com/api/v1/chatbot/adicionar"

# Catálogo sincronizado com o Documento de Especificação Funcional
perguntas_iniciais = [
    {
        "categoria": "Financeiro",
        "pergunta": "Quais são as formas de pagamento aceitas?",
        "resposta": "Aceitamos cartões de crédito (Visa, Mastercard, Elo, Amex), cartões de débito e pagamento via PIX."
    },
    {
        "categoria": "Financeiro",
        "pergunta": "Como faço para mudar ou fazer upgrade no meu plano?",
        "resposta": "Vá até 'Minha Conta', selecione 'Minha Assinatura' e clique em 'Alterar plano'."
    },
    {
        "categoria": "Financeiro",
        "pergunta": "A minha fatura foi cobrada em duplicidade?",
        "resposta": "Acesse o painel 'Pagamentos' e clique em 'Contestar cobrança', ou acione um atendente."
    },
    {
        "categoria": "Conta",
        "pergunta": "Esqueci a minha senha, como posso recuperá-la?",
        "resposta": "Na tela de login, clique em 'Esqueci minha senha'. Enviaremos um e-mail com as instruções."
    },
    {
        "categoria": "Conta",
        "pergunta": "Como criar um perfil infantil (Kids)?",
        "resposta": "Acesse 'Gerenciar Perfis', clique em 'Adicionar Perfil' e ative a opção 'Perfil Infantil'."
    },
    {
        "categoria": "Conta",
        "pergunta": "Como faço para excluir o meu perfil secundário?",
        "resposta": "Acesse 'Gerenciar Perfis', selecione o perfil que deseja remover e clique em 'Excluir perfil'."
    },
    {
        "categoria": "Conteúdo",
        "pergunta": "Posso baixar filmes e séries para assistir offline?",
        "resposta": "Sim! No app mobile, clique no ícone de download ao lado do episódio desejado."
    },
    {
        "categoria": "Conteúdo",
        "pergunta": "Consigo assistir à programação ao vivo?",
        "resposta": "Sim, acesse a seção 'Ao Vivo' no menu principal para acompanhar os canais disponíveis."
    },
    {
        "categoria": "Conteúdo",
        "pergunta": "Como faço para assistir aos jogos do Flamengo?",
        "resposta": "Verifique se o seu plano inclui o pacote Premiere ou acesse a transmissão via SporTV."
    },
    {
        "categoria": "Conteúdo",
        "pergunta": "Por quanto tempo os downloads ficam disponíveis?",
        "resposta": "Títulos baixados permanecem salvos por até 30 dias (ou 48h após o início da reprodução)."
    },
    {
        "categoria": "Suporte",
        "pergunta": "O aplicativo fecha sozinho durante a reprodução.",
        "resposta": "Verifique atualizações, limpe o cache do dispositivo ou reinstale o aplicativo."
    },
    {
        "categoria": "Suporte",
        "pergunta": "Como mudar o idioma ou ativar legendas?",
        "resposta": "Durante a reprodução, clique no ícone de engrenagem ou balão de diálogo."
    },
    {
        "categoria": "Suporte",
        "pergunta": "Minha Smart TV não tem o aplicativo.",
        "resposta": "Utilize dispositivos como Chromecast, Apple TV ou Roku Express na entrada HDMI."
    }
]

def enviar_dados():
    adicionadas = 0
    print("Iniciando o envio de dados para o Render...\n")

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

    print(f"\nConcluído! {adicionadas} novas perguntas foram registradas na nuvem.")

if __name__ == "__main__":
    enviar_dados()