# ---------------------------------------------------
# Rotas Analíticas do Dashboard
# Criado por R.P.
# ---------------------------------------------------
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from app.core.database import get_db
from app.models import faq_model
from app.schemas import dashboard_schema

router = APIRouter()

@router.get("/resumo", response_model=dashboard_schema.ResumoDashboard)
def obter_resumo_geral(db: Session = Depends(get_db)):
    """Retorna o total de consultas e a proporção de respostas bem-sucedidas."""
    total = db.query(faq_model.HistoricoChat).count()

    respondidas = db.query(faq_model.HistoricoChat).filter(
        faq_model.HistoricoChat.respondida == True
    ).count()

    return {
        "total_consultas": total,
        "perguntas_respondidas": respondidas,
        "perguntas_sem_resposta": total - respondidas
    }

@router.get("/categorias", response_model=list[dashboard_schema.DistribuicaoCategoria])
def distribuicao_por_categoria(db: Session = Depends(get_db)):
    """Retorna o volume de atendimentos agrupado por categoria no banco de dados."""
    resultado = db.query(
        faq_model.PerguntaFAQ.categoria,
        func.count(faq_model.HistoricoChat.id).label("quantidade")
    ).join(
        faq_model.HistoricoChat,
        faq_model.PerguntaFAQ.id == faq_model.HistoricoChat.pergunta_faq_id
    ).group_by(
        faq_model.PerguntaFAQ.categoria
    ).all()

    return [{"categoria": r.categoria, "quantidade": r.quantidade} for r in resultado]

@router.get("/sem-resposta", response_model=list[dashboard_schema.PerguntaSemResposta])
def perguntas_nao_respondidas(db: Session = Depends(get_db)):
    """Lista as últimas 10 perguntas que precisaram de fallback para análise de curadoria."""
    resultados = db.query(faq_model.HistoricoChat).filter(
        faq_model.HistoricoChat.respondida == False
    ).order_by(desc(faq_model.HistoricoChat.data_hora)).limit(10).all()

    # Validação de segurança adicionada: garante que data_hora não é None antes de formatar
    return [
        {
            "pergunta_usuario": r.pergunta_usuario,
            "data_hora": r.data_hora.strftime("%d/%m/%Y %H:%M") if r.data_hora else "Data Indisponível"
        } for r in resultados
    ]

@router.get("/frequentes")
def perguntas_mais_frequentes(db: Session = Depends(get_db)):
    """Retorna o Top 5 das perguntas mais realizadas no chat."""
    resultados = db.query(
        faq_model.HistoricoChat.pergunta_usuario,
        func.count(faq_model.HistoricoChat.id).label("quantidade")
    ).group_by(
        faq_model.HistoricoChat.pergunta_usuario
    ).order_by(
        desc("quantidade")
    ).limit(5).all()

    return [{"pergunta": r.pergunta_usuario, "quantidade": r.quantidade} for r in resultados]