from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config import Config

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo=True,
    poolsize=5,
    max_overflow=10
)

session_maker = async_sessionmaker(engine)
