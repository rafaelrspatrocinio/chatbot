# ---------------------------------------------------
# Script para popular a base de dados em Produção
# Criado por R.P.
# ---------------------------------------------------
import requests

# A URL oficial da sua API no Render
BASE_URL = "https://chatbot-v8a5.onrender.com/api/v1/chatbot/adicionar"

perguntas_iniciais = [
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
    },
    {
        "pergunta": "Como faço para assistir aos jogos do Flamengo ao vivo?",
        "resposta": "Você pode acompanhar as partidas ao vivo garantindo que o seu plano inclui o pacote Premiere ou acessando a transmissão simultânea do SporTV e da TV aberta, dependendo da disponibilidade do campeonato.",
        "categoria": "Conteúdo"
    },
    {
        "pergunta": "Minha Smart TV não tem o aplicativo, o que fazer?",
        "resposta": "Se a sua TV não possui o nosso aplicativo na loja oficial, você pode utilizar aparelhos como Chromecast, Apple TV, Roku Express ou Amazon Fire TV Stick conectados à entrada HDMI para transmitir o conteúdo.",
        "categoria": "Suporte Técnico"
    },
    {
        "pergunta": "Como criar um perfil infantil (Kids)?",
        "resposta": "Acesse 'Gerenciar Perfis', clique em 'Adicionar Perfil' e ative a opção 'Perfil Infantil'. Isso aplicará um filtro automático para que apenas conteúdos adequados para crianças sejam exibidos.",
        "categoria": "Conta"
    },
    {
        "pergunta": "Como faço para mudar ou fazer upgrade no meu plano?",
        "resposta": "Vá até 'Minha Conta', selecione 'Minha Assinatura' e clique em 'Alterar plano'. Escolha a nova opção desejada (como adicionar canais ao vivo) e confirme. A mudança pode ter efeito imediato ou no próximo ciclo de faturamento.",
        "categoria": "Financeiro"
    },
    {
        "pergunta": "Por quanto tempo os downloads ficam disponíveis offline?",
        "resposta": "Os títulos baixados permanecem salvos por até 30 dias no seu dispositivo. Porém, após você apertar o play pela primeira vez sem internet, terá 48 horas para terminar de assistir.",
        "categoria": "Conteúdo"
    },
    {
        "pergunta": "Não estou encontrando uma novela ou série específica, por quê?",
        "resposta": "Nosso catálogo é atualizado constantemente. Alguns conteúdos podem sair da plataforma temporariamente devido a renovações de contratos de licenciamento ou direitos autorais.",
        "categoria": "Conteúdo"
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