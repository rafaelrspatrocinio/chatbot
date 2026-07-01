import { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import { Send } from 'lucide-react';

export default function Chatbot() {
  const [mensagens, setMensagens] = useState([
    { remetente: 'bot', texto: 'Olá! Sou o assistente virtual da Globo. Como posso ajudar hoje?' }
  ]);
  const [input, setInput] = useState('');
  const fimDoChatRef = useRef(null);

  // Faz o scroll automático para a última mensagem
  useEffect(() => {
    fimDoChatRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [mensagens]);

  const enviarPergunta = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    // Adiciona a pergunta do utilizador ao ecrã
    const novaMensagemUsuario = { remetente: 'usuario', texto: input };
    setMensagens((prev) => [...prev, novaMensagemUsuario]);
    const textoPergunta = input;
    setInput('');

    try {
      // Chama a nossa API em Python no Docker
      const resposta = await axios.post('https://chatbot-v8a5.onrender.com/api/v1/chatbot/perguntar', {
        pergunta: textoPergunta
      });

      // Adiciona a resposta do bot ao ecrã
      setMensagens((prev) => [...prev, { remetente: 'bot', texto: resposta.data.resposta }]);
    } catch (erro) {
      setMensagens((prev) => [...prev, {
        remetente: 'bot',
        texto: 'Desculpe, ocorreu um erro de ligação com o servidor.'
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
          </div>
        ))}
        <div ref={fimDoChatRef} />
      </div>

      <form className="chat-input-area" onSubmit={enviarPergunta}>
        <input
          type="text"
          placeholder="Escreva a sua dúvida aqui..."
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