from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

from app.core.config import settings

# The Engine is the core interface to the database.
# It's configured with our database URL.

engine = create_engine(settings.DATABASE_URL, isolation_level="AUTOCOMMIT")

if not database_exists(engine.url):
    create_database(engine.url)

# A SessionLocal class is a "factory" for creating new database sessions.
# Each session is a single conversation with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is a class that our database models will inherit from.
# SQLAlchemy uses it to map our Python objects to database tables.
Base = declarative_base()