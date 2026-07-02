import { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send } from 'lucide-react';

export default function Chatbot() {
  const [mensagens, setMensagens] = useState([
    {
      remetente: 'bot',
      texto: 'Olá! Sou o assistente virtual da Globo. Como posso ajudar hoje? Escolha uma das categorias abaixo ou digite sua dúvida:',
      opcoes: ['Financeiro', 'Conta', 'Conteúdo', 'Suporte Técnico']
    }
  ]);
  const [input, setInput] = useState('');
  const fimDoChatRef = useRef(null);

  // Faz o scroll automático para a última mensagem
  useEffect(() => {
    fimDoChatRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [mensagens]);

  const enviarPergunta = async (eventoOuTexto) => {
    // Previne o recarregamento da página se vier do form de envio
    if (eventoOuTexto && eventoOuTexto.preventDefault) {
      eventoOuTexto.preventDefault();
    }

    // Identifica se a chamada veio do botão (string) ou do input de texto
    const textoPergunta = typeof eventoOuTexto === 'string' ? eventoOuTexto : input;

    if (!textoPergunta.trim()) return;

    // Adiciona a pergunta do usuário à tela
    const novaMensagemUsuario = { remetente: 'usuario', texto: textoPergunta };
    setMensagens((prev) => [...prev, novaMensagemUsuario]);

    // Só limpa o input se a mensagem foi enviada pelo campo de texto
    if (typeof eventoOuTexto !== 'string') {
      setInput('');
    }

    try {
      // Chama a nossa API em Python no Docker/Render
      const resposta = await axios.post('https://chatbot-v8a5.onrender.com/api/v1/chatbot/perguntar', {
        pergunta: textoPergunta
      });

      // Adiciona a resposta do bot à tela
      setMensagens((prev) => [...prev, { remetente: 'bot', texto: resposta.data.resposta }]);
    } catch (erro) {
      setMensagens((prev) => [...prev, {
        remetente: 'bot',
        texto: 'Desculpe, ocorreu um erro de conexão com o servidor.'
      }]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Atendimento Automático</h2>
        <p>Respostas em tempo real da base de conhecimento</p>
      </div>

      <div className="chat-mensagens">
        {mensagens.map((msg, index) => (
          <div key={index} className={`mensagem-wrapper ${msg.remetente}`}>
            <div className={`bolha-mensagem ${msg.remetente}`}>
              {msg.texto}
            </div>

            {/* Renderiza os botões de opção se a mensagem possuir essa propriedade */}
            {msg.opcoes && (
              <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginTop: '10px' }}>
                {msg.opcoes.map((opcao, i) => (
                  <button
                    key={i}
                    onClick={() => enviarPergunta(opcao)}
                    type="button"
                    style={{
                      backgroundColor: '#e0f2fe',
                      color: '#0369a1',
                      border: '1px solid #bae6fd',
                      padding: '6px 12px',
                      borderRadius: '16px',
                      cursor: 'pointer',
                      fontSize: '14px',
                      fontWeight: 'bold'
                    }}
                  >
                    {opcao}
                  </button>
                ))}
              </div>
            )}

          </div>
        ))}
        <div ref={fimDoChatRef} />
      </div>

      <form className="chat-input-area" onSubmit={enviarPergunta}>
        <input
          type="text"
          placeholder="Digite sua dúvida aqui..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit" className="btn-enviar">
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}