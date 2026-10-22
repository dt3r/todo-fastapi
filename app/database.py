from sqlalchemy import URL, create_engine, text, insert
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from config import settings

sync_engine = create_engine(
    url = settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
    

)

session_factory = sessionmaker(sync_engine)

class Base(DeclarativeBase):
    pass



