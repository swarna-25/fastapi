import time

import psycopg2
from psycopg2.extras import RealDictCursor 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#format-'postgressql://<username>:<password>@<ip-address/hostname>:<port>/<databse_name>'
# SQLALCHEMY_DATABASE_URL='postgresql://jinendra.soni:Jine1921@127.0.0.1:5432/fastapi'   
SQLALCHEMY_DATABASE_URL= f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'


engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn=psycopg2.connect ( host='127.0.0.1',database='fastapi',user='jinendra.soni',
#                             password='Jine1921@#@#@#@#',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to Database failed")
#         print("Error: " ,error)
#         time.sleep(2)