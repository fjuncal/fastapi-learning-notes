from fastapi import FastAPI

import user_route
from database import Base, engine

#Cria a aplicação FastAPI
#Equivalente a: @SpringBootApplication
app = FastAPI()

#Cria todas as tabelas do banco com base nos modelos (User, etc)
#Equivalente a: spring.jpa.hibernate.ddl-auto=update
Base.metadata.create_all(bind=engine)

#Importa e registra todas as rotas definidas no user_router
#Equivalente a registrar os controllers no Spring
app.include_router(user_route.router)
