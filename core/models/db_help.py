from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from core.config import settings


class DateBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )


db_helper = DateBaseHelper(url=settings.db_url, echo=settings.db_echo)
