from pydantic import BaseModel

class PerguntaFAQBase(BaseModel):
    pergunta: str
    resposta: str
    categoria: str

class PerguntaFAQCreate(PerguntaFAQBase):
    pass

class PerguntaFAQResponse(PerguntaFAQBase):
    id: int

    class Config:
        from_attributes = True