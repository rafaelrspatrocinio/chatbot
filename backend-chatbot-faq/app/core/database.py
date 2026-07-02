# ---------------------------------------------------
# Configuração de conexão com o Banco de Dados
# Criado por R.P.
# ---------------------------------------------------
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Pega a URL do banco nas variáveis de ambiente. Se não achar, usa o SQLite local.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chatbot.db")

# O SQLAlchemy moderno exige que a URL comece com "postgresql://"
# Mas o Render costuma entregar como "postgres://". Este bloco corrige isso.
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

# O SQLite precisa de argumentos especiais, o Postgres não.
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()