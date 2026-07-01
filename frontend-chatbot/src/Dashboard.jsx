import { useEffect, useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Dashboard() {
  const [resumo, setResumo] = useState({ total_consultas: 0, perguntas_respondidas: 0, perguntas_sem_resposta: 0 });
  const [categorias, setCategorias] = useState([]);

  useEffect(() => {
    // Busca os dados da API Python que criámos anteriormente
    axios.get('http://localhost:8000/api/v1/dashboard/resumo').then(res => setResumo(res.data));
    axios.get('http://localhost:8000/api/v1/dashboard/categorias').then(res => setCategorias(res.data));
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
    </div>
  );
}