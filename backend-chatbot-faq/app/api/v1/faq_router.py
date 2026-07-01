from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import faq_model
from app.schemas import faq_schema

# Cria o roteador para o módulo FAQ
router = APIRouter()

@router.post("/", response_model=faq_schema.PerguntaFAQResponse)
def criar_pergunta_faq(faq: faq_schema.PerguntaFAQCreate, db: Session = Depends(get_db)):
    nova_pergunta = faq_model.PerguntaFAQ(
        pergunta=faq.pergunta,
        resposta=faq.resposta,
        categoria=faq.categoria
    )
    db.add(nova_pergunta)
    db.commit()
    db.refresh(nova_pergunta)
    return nova_pergunta

@router.get("/", response_model=list[faq_schema.PerguntaFAQResponse])
def listar_perguntas(db: Session = Depends(get_db)):
    return db.query(faq_model.PerguntaFAQ).all()