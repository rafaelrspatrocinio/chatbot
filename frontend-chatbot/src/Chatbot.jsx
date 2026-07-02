import React, { useState, useRef, useEffect } from 'react';
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

  // 1. Referência para o auto-scroll
  const fimDoChatRef = useRef(null);

  // 2. Efeito que faz a rolagem sempre que uma nova mensagem entra
  useEffect(() => {
    fimDoChatRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [mensagens]);

  const enviarPergunta = async (eventoOuTexto) => {
    // Previne o recarregamento da página (acionado ao pressionar Enter no form)
    if (eventoOuTexto && eventoOuTexto.preventDefault) {
      eventoOuTexto.preventDefault();
    }

    // Identifica se a chamada veio do botão rápido (string) ou do input de texto
    const textoPergunta = typeof eventoOuTexto === 'string' ? eventoOuTexto : input;

    if (!textoPergunta.trim()) return;

    // Adiciona a pergunta do utilizador ao ecrã
    const novaMensagemUsuario = { remetente: 'usuario', texto: textoPergunta };
    setMensagens((prev) => [...prev, novaMensagemUsuario]);

    // Limpa o input apenas se a mensagem foi enviada pelo campo de texto
    if (typeof eventoOuTexto !== 'string') {
      setInput('');
    }

    try {
      const resposta = await axios.post('https://chatbot-v8a5.onrender.com/api/v1/chatbot/perguntar', {
        pergunta: textoPergunta
      });

      // Adiciona a resposta da base de conhecimento
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

            {/* Renderiza os botões de opção rápida */}
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
        {/* Âncora invisível onde o scroll automático vai parar */}
        <div ref={fimDoChatRef} />
      </div>

      {/* O uso do <form> permite que a tecla "Enter" acione o envio automaticamente */}
      <form className="chat-input-area" onSubmit={enviarPergunta}>
        <input
          type="text"
          placeholder="Digite a sua dúvida aqui..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        {/* Adicionado aria-label para acessibilidade em leitores de ecrã */}
        <button type="submit" className="btn-enviar" aria-label="Enviar mensagem">
          <Send size={18} />
        </button>
      </form>
    </div>
  );
}