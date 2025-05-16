from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate

#✅ 4. Por que usamos User(**user_data.dict()) no services.py?
#user_data é um UserCreate, um Pydantic object.
#.dict() transforma em: {"name": "Fulano", "email": "fulano@email.com"}
#O ** desestrutura e passa os dados como argumentos nomeados: User(name="Fulano", email="fulano@email.com")



#✅ 5. Por que usamos add, commit e refresh?
#Sempre que você cria, precisa fazer os três se quiser:
#Salvar no banco
#Obter os dados atualizados (como o ID gerado)

def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.dict())
    db.add(user) # adiciona à sessão
    db.commit() # salva no banco
    db.refresh(user) # recarrega com o ID gerado
    return user


#✅ 6. Sempre temos que passar o Session para os serviços?
#O Session é como o EntityManager do JPA.
#Permite acessar, consultar, criar, etc.
#db.query(User) é uma consulta SQL SELECT.
#Equivale a: SELECT * FROM users em SQL.
def get_users(db: Session):
    return db.query(User).all()