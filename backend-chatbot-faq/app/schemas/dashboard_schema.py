from pydantic import BaseModel

class ResumoDashboard(BaseModel):
    total_consultas: int
    perguntas_respondidas: int
    perguntas_sem_resposta: int

class DistribuicaoCategoria(BaseModel):
    categoria: str
    quantidade: int

class PerguntaSemResposta(BaseModel):
    pergunta_usuario: str
    data_hora: str