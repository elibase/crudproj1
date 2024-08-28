# used for creating the sqlalchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# creating database url for sqlalchemy
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:AzRt63_3!fd@crudproj1_School/db"

# creating the sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create a session local class
SessionLocal = SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()