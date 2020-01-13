from contextlib import contextmanager


async def create_aiohttp_session(aiohttp, loop):
    session = aiohttp.ClientSession(loop=loop)
    return session


async def close_aiohttp_session(session):
    await session.close()


async def close_redis_connection(redis):
    keys = await redis.keys("*")
    for key in keys:
        await redis.delete(key)
    redis.close()
    await redis.wait_closed()


def get_db_url(config, db='postgresql', adapter='psycopg2'):
    url = f'{db}+{adapter}://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}'
    return url


@contextmanager
def db_session(app):
    session = app.sqlalchemy.orm.scoped_session(
        app.sqlalchemy.orm.sessionmaker(
            autocommit=False,
            autoflush=True,
            bind=app.db_engine
        )
    )
    try:
        yield session
    except app.sqlalchemy.exc.SQLAlchemyError as e:
        session.rollback()
    finally:
        session.remove()
