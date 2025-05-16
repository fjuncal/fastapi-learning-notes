from fastapi import Depends
from fastapi.routing import APIRoute, APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import UserOut, UserCreate
from services import create_user, get_users

router = APIRouter(prefix="/users", tags=["Users"])

#✅ 7. Por que criamos o get_db() no user_router.py?
#Isso é um "gerador" de sessão.
#Ele abre e fecha a conexão com o banco automaticamente.
#Evita vazamento de conexão.
#Equivalente a um @Transactional com @Autowired EntityManager no Spring.

def get_db():
    db = SessionLocal()
    try:
        yield db
        # O yield transforma a função em um gerador.
        # Ele pausa a execução e entrega o valor (db) para o FastAPI.
        # Depois que o endpoint termina, o código após o yield é executado (db.close()).
        # Isso garante que a conexão com o banco seja sempre fechada corretamente.

    finally:
        db.close()


#✅ 8. O que significa db: Session = Depends(get_db)?
#Equivale ao @Autowired do Spring
#Depends(get_db) = FastAPI injeta o db automaticamente.
#Isso é o sistema de injeção de dependência do FastAPI.
#Não precisa chamar get_db() manualmente.
#Em cada request, o FastAPI:
#Cria o db
#Injeta no parâmetro
#Fecha no final

@router.post("/", response_model=UserOut)
def create(user: UserCreate, db: SessionLocal = Depends(get_db)):
    return create_user(db, user)

@router.get("/", response_model=list[UserOut])
def list_users(db: Session = Depends(get_db)):
    return get_users(db)