import { useEffect, useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Dashboard() {
  const [resumo, setResumo] = useState({ total_consultas: 0, perguntas_respondidas: 0, perguntas_sem_resposta: 0 });
  const [categorias, setCategorias] = useState([]);
  const [frequentes, setFrequentes] = useState([]);

  useEffect(() => {
      axios.get('https://chatbot-v8a5.onrender.com/api/v1/dashboard/resumo').then(res => setResumo(res.data));
      axios.get('https://chatbot-v8a5.onrender.com/api/v1/dashboard/categorias').then(res => setCategorias(res.data));
      axios.get('https://chatbot-v8a5.onrender.com/api/v1/dashboard/frequentes').then(res => setFrequentes(res.data));
    }, []);

  return (
    <div className="dashboard-container">
      <h3>Painel Analítico de Atendimento</h3>

      {/* Cartões de Resumo */}
      <div className="stats-grid">
        <div className="stat-card"><h4>Total Consultas</h4><p>{resumo.total_consultas}</p></div>
        <div className="stat-card"><h4>Respondidas</h4><p>{resumo.perguntas_respondidas}</p></div>
        <div className="stat-card"><h4>Pendentes</h4><p>{resumo.perguntas_sem_resposta}</p></div>
      </div>

      {/* Gráfico de Categorias */}
      <div className="chart-container">
        <h4>Consultas por Categoria</h4>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={categorias}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="categoria" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="quantidade" fill="#2563eb" />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="chart-container" style={{ marginTop: '20px' }}>
              <h4 style={{ marginBottom: '16px' }}>Top 5 - Perguntas Mais Frequentes</h4>
              <div style={{ overflowX: 'auto' }}>
                <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left' }}>
                  <thead>
                    <tr style={{ backgroundColor: '#f9fafb', borderBottom: '2px solid #e5e7eb' }}>
                      <th style={{ padding: '12px', color: '#4b5563', fontSize: '14px' }}>Pergunta do Utilizador</th>
                      <th style={{ padding: '12px', color: '#4b5563', fontSize: '14px', width: '100px', textAlign: 'center' }}>Volume</th>
                    </tr>
                  </thead>
                  <tbody>
                    {frequentes.map((item, index) => (
                      <tr key={index} style={{ borderBottom: '1px solid #e5e7eb' }}>
                        <td style={{ padding: '12px', fontSize: '14px', color: '#1f2937' }}>
                          {item.pergunta}
                        </td>
                        <td style={{ padding: '12px', fontSize: '14px', fontWeight: 'bold', color: '#2563eb', textAlign: 'center' }}>
                          {item.quantidade}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
                {frequentes.length === 0 && (
                  <p style={{ padding: '20px', textAlign: 'center', color: '#9ca3af' }}>Nenhum dado registado ainda.</p>
                )}
              </div>
            </div>
    </div>
  );
}