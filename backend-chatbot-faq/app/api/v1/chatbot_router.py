from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.database import get_db
from app.models import faq_model
from app.schemas import chatbot_schema

router = APIRouter()

# Schema para validar os dados que vêm do seu script
class FAQCreate(BaseModel):
    pergunta: str
    resposta: str
    categoria: str

@router.post("/perguntar", response_model=chatbot_schema.RespostaChatbot)
def perguntar_chatbot(consulta: chatbot_schema.PerguntaUsuario, db: Session = Depends(get_db)):

    # Pesquisa simples utilizando LIKE para encontrar palavras semelhantes
    termo_busca = f"%{consulta.pergunta}%"

    pergunta_faq = db.query(faq_model.PerguntaFAQ).filter(
        faq_model.PerguntaFAQ.pergunta.like(termo_busca)
    ).first()

    if pergunta_faq:
        # Encontrou resposta: Regista no histórico associando o ID
        novo_historico = faq_model.HistoricoChat(
            pergunta_usuario=consulta.pergunta,
            pergunta_faq_id=pergunta_faq.id,
            respondida=True
        )
        db.add(novo_historico)
        db.commit()

        return {
            "pergunta_original": consulta.pergunta,
            "resposta": pergunta_faq.resposta,
            "encontrou_resposta": True
        }
    else:
        # Não encontrou: Regista no histórico com respondida=False e ID nulo
        novo_historico = faq_model.HistoricoChat(
            pergunta_usuario=consulta.pergunta,
            pergunta_faq_id=None,
            respondida=False
        )
        db.add(novo_historico)
        db.commit()

        return {
            "pergunta_original": consulta.pergunta,
            "resposta": "Desculpe, ainda não tenho a resposta para essa dúvida. O seu pedido foi registado e a nossa equipa vai analisá-lo em breve!",
            "encontrou_resposta": False
        }

@router.post("/adicionar")
def adicionar_faq(faq: FAQCreate, db: Session = Depends(get_db)):
    # Verifica se já existe para não duplicar
    existe = db.query(faq_model.PerguntaFAQ).filter(faq_model.PerguntaFAQ.pergunta == faq.pergunta).first()

    if existe:
        return {"status": "erro", "mensagem": "Pergunta já existe"}

    nova_pergunta = faq_model.PerguntaFAQ(
        pergunta=faq.pergunta,
        resposta=faq.resposta,
        categoria=faq.categoria
    )
    db.add(nova_pergunta)
    db.commit()
    db.refresh(nova_pergunta)
    return {"status": "sucesso", "id": nova_pergunta.id}