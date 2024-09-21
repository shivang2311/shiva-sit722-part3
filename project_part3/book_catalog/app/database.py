from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://shivangpart3_user:b36T94zE26pqYFKg6Y5S1Q2VdfnzBWCa@dpg-crjf7tdumphs73d03ei0-a.oregon-postgres.render.com/shivangpart3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
