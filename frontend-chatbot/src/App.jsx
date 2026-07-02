import { useState } from 'react'
import { MessageSquare, BarChart3 } from 'lucide-react'
import Chatbot from './Chatbot'
import './index.css'
import Dashboard from './Dashboard'
import Login from './Login'

function App() {
  const [abaAtiva, setAbaAtiva] = useState('chatbot')
  // Estado para controlar se o utilizador já fez login
  const [autenticado, setAutenticado] = useState(false)

  return (
    <div className="app-container">
      <aside className="sidebar">
        <div className="sidebar-header">
          <div className="logo-box">G</div>
          <h2>Globo FAQ</h2>
        </div>

        <nav className="sidebar-nav">
          <button
            className={`nav-button ${abaAtiva === 'chatbot' ? 'active' : ''}`}
            onClick={() => setAbaAtiva('chatbot')}
          >
            <MessageSquare size={20} />
            Atendimento
          </button>

          <button
            className={`nav-button ${abaAtiva === 'dashboard' ? 'active' : ''}`}
            onClick={() => setAbaAtiva('dashboard')}
          >
            <BarChart3 size={20} />
            Painel Analítico
          </button>
        </nav>

        <div className="sidebar-footer">&copy; 2026 R.P.</div>
      </aside>

      <main className="main-content">
        {abaAtiva === 'chatbot' ? (
          <Chatbot />  // <-- Renderiza o chat normalmente
        ) : (
          // Se clicou no dashboard, verifica se está autenticado
          autenticado ? (
            <Dashboard />
          ) : (
            <Login onLoginSucesso={() => setAutenticado(true)} />
          )
        )}
      </main>
    </div>
  )
}

export default App