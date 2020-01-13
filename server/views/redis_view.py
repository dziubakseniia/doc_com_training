from sanic.response import text
from sanic.views import HTTPMethodView

from src.controllers.redis_controller import RedisController


class RedisView(HTTPMethodView):
    def __init__(self):
        self.controller = RedisController()

    async def post(self, request):
        app = request.app
        json = await self.controller.set_status(app)
        return text(json)

    async def get(self, request):
        app = request.app
        value = await self.controller.get_status(app, request)
        return text(value)
