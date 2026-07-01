from pydantic import BaseModel

class PerguntaUsuario(BaseModel):
    pergunta: str

class RespostaChatbot(BaseModel):
    pergunta_original: str
    resposta: str
    encontrou_resposta: bool