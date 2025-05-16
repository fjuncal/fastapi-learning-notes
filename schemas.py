from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str


#✅ 3. Por que usamos UserCreate dentro de UserOut? E o que é Config?
#🔹 UserOut(UserCreate)
#Reaproveita os campos (name, email) sem reescrever.

#🔹 Config.orm_mode = True
#Permite que o Pydantic entenda objetos ORM (como User) diretamente.
#Sem isso, ele esperaria um dict, e não um modelo ORM.
#Isso permite fazer: return db_user  # mesmo sendo um objeto SQLAlchemy


class UserOut(UserCreate):
    id: int

    class Config:
        orm_mode = True