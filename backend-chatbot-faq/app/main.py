# ---------------------------------------------------
# Cliente: Grupo Globo
# Projeto: Chatbot de FAQ com Dashboard Analítico
# ---------------------------------------------------

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- 1. Nova importação
from app.api.v1 import faq_router, chatbot_router, dashboard_router
from app.core.database import engine
from app.models import faq_model

faq_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Globo FAQ Chatbot API",
    description="Backend para gestão de conhecimento e histórico do chatbot.",
    version="1.0.0"
)

# 2. Configuração do CORS (Permite que o React converse com a API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chatbot-theta-inky-41.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(faq_router.router, prefix="/api/v1/faq", tags=["Base de Conhecimento FAQ"])
app.include_router(chatbot_router.router, prefix="/api/v1/chatbot", tags=["Motor do Chatbot"])
app.include_router(dashboard_router.router, prefix="/api/v1/dashboard", tags=["Dashboard Analítico"])

@app.get("/", tags=["Health Check"])
def health_check():
    return {"status": "Online", "ambiente": "Produção", "cliente": "Globo"}