from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL= "sqlite:///./test.db"

#Cria a conexão com o banco de dados, engine é o objeto que representa a conexão com o banco, connect_args é usado no SQLite para permitir múltiplas threads
#equivalente ao que o Spring Boot faz via DataSource automático
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

#Cria sessões de acesso ao banco (equivalente ao EntityManager no JPA)
#Cria uma fábrica de sessões. Sempre que precisar acessar o banco, você cria uma sessão com: db = SessionLocal()
#Equivale ao uso de @PersistenceContext EntityManager em
#Cada vez que você chama SessionLocal(), você está criando uma nova sessão transacional
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Cria a classe base para os modelos (entidades). Cada model vai herdar essa Base, igual herda Entity no Java
#Parecido com o que o Spring faz com @Entity + JPA metamodel
#Equivale a dizer: “todas as entidades vão herdar de um @MappedSuperclass
Base = declarative_base()