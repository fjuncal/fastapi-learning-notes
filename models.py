from sqlalchemy import Column, Integer, String
from database import Base


#✅ 2. Por que usamos Base em models.py?
#Isso é igual dizer: "essa classe representa uma tabela do banco".
#A Base registra o modelo dentro do SQLAlchemy.
#Sem herdar de Base, o User não seria reconhecido como entidade para o create_all().

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)