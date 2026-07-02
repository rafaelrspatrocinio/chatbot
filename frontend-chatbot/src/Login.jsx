/* ---------------------------------------------------
 * Ecrã de Login para Proteção do Dashboard
 * Criado por R.P.
 * --------------------------------------------------- */
import React, { useState } from 'react';
import axios from 'axios';
import { Lock } from 'lucide-react';

export default function Login({ onLoginSucesso }) {
  const [usuario, setUsuario] = useState('');
  const [senha, setSenha] = useState('');
  const [erro, setErro] = useState('');
  const [carregando, setCarregando] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setErro('');
    setCarregando(true);

    try {
      const resposta = await axios.post('https://chatbot-v8a5.onrender.com/api/v1/dashboard/login', {
        usuario: usuario,
        senha: senha
      });

      if (resposta.data.status === 'sucesso') {
        onLoginSucesso(); // Liberta o acesso ao Dashboard!
      }
    } catch (err) {
      setErro('Credenciais inválidas. Tente novamente.');
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100%' }}>
      <div style={{ background: 'white', padding: '40px', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)', width: '100%', maxWidth: '400px' }}>
        <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '20px', color: '#2563eb' }}>
          <Lock size={48} />
        </div>
        <h2 style={{ textAlign: 'center', marginBottom: '24px', color: '#1f2937' }}>Acesso Restrito</h2>

        {erro && <div style={{ background: '#fee2e2', color: '#b91c1c', padding: '10px', borderRadius: '6px', marginBottom: '16px', fontSize: '14px', textAlign: 'center' }}>{erro}</div>}

        <form onSubmit={handleLogin} style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
          <input
            type="text"
            placeholder="Utilizador (ex: admin)"
            value={usuario}
            onChange={(e) => setUsuario(e.target.value)}
            style={{ padding: '12px', borderRadius: '6px', border: '1px solid #d1d5db', outline: 'none' }}
          />
          <input
            type="password"
            placeholder="Palavra-passe (ex: globo123)"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            style={{ padding: '12px', borderRadius: '6px', border: '1px solid #d1d5db', outline: 'none' }}
          />
          <button
            type="submit"
            disabled={carregando}
            style={{ padding: '12px', background: '#2563eb', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer', fontWeight: 'bold', marginTop: '8px' }}
          >
            {carregando ? 'A verificar...' : 'Entrar'}
          </button>
        </form>
      </div>
    </div>
  );
}