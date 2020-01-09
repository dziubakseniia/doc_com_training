import aiohttp
import sqlalchemy
from sanic import Sanic

import utils
from routes import setup_routes

from src.models.base_model import Base

app = Sanic("app")

@app.listener('before_server_start')
async def before_server_start(app, loop):
    app.aiohttp_session = await utils.create_aiohttp_session(aiohttp, loop)
    app.config.from_pyfile("config.py")
    
    app.sqlalchemy = sqlalchemy
    db_url = utils.get_db_url(app.config)
    app.db_engine = sqlalchemy.create_engine(db_url)

    Base.metadata.create_all(app.db_engine)

@app.listener('after_server_stop')
async def after_server_stop(app, loop):
    await utils.close_aiohttp_session(app.aiohttp_session)

    app.db_engine.dispose()

def run():
    setup_routes(app)
    app.run(host='server', port=8004)
    return app

if __name__ == '__main__':
    run()
