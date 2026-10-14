from sqlalchemy import URL, create_engine, text
from config import settings


engine = create_engine(
    url = settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,

)

