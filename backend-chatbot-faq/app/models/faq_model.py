from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from datetime import datetime
from app.core.database import Base

class PerguntaFAQ(Base):
    __tablename__ = "perguntas_faq"

    id = Column(Integer, primary_key=True, index=True)
    pergunta = Column(String, index=True)
    resposta = Column(String)
    categoria = Column(String)

class HistoricoChat(Base):
    __tablename__ = "historico_chat"

    id = Column(Integer, primary_key=True, index=True)
    pergunta_usuario = Column(String)
    pergunta_faq_id = Column(Integer, ForeignKey("perguntas_faq.id"), nullable=True)
    respondida = Column(Boolean, default=False)
    data_hora = Column(DateTime, default=datetime.utcnow)