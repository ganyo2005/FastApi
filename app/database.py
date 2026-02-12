from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker   
import psycopg2,time 
from psycopg2.extras import  RealDictCursor
from .config import settings


SQLALCHEMY_DATABASE_URL=f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()


# while True:
#     try:
#         conn=psycopg2.connect(host='localhost',database='FastAPI',user='postgres',password='nick@ktu',cursor_factory=
#                             RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was succesfull")
#         break
#     except Exception as error:
#         print("Problem connecting to database")
#         time.sleep(2)
       



# my_post=[{"title":"This is the title","content":"content 1","id":1},{"title":"title 2","content":"content 2","id":2}]


