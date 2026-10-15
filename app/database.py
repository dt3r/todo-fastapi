from sqlalchemy import URL, create_engine, text
from config import settings
from app.models.models import metadata_object

sync_engine = create_engine(
    url = settings.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,

)

def create_tables():
    metadata_object.create_all(sync_engine)