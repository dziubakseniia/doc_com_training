from sanic.response import text
from sanic.views import HTTPMethodView

from decorators import uppercase


class TestStatusView(HTTPMethodView):
    async def get(self, request):
        return text("Test GET")
    
    @uppercase
    async def post(self, request):
        return text("test post")
