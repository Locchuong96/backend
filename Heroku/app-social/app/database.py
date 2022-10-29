from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#f"postgresql://<{username}>:<{password}>@<{ip_address}/{hostname}>/<{database_name}>"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL) # engine to connect datanase

SessionLocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) # for taking with database

Base = declarative_base() # Model Base for create table, alembic can access it

# Dependency [request] -> [create session] -> [create sql] -> [close session]
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()