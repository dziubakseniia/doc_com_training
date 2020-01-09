from sanic.views import HTTPMethodView
from sanic.response import text

from decorators import uppercase

class TestStatusView(HTTPMethodView):
    async def get(self, request):
        return text("Test GET")
    
    @uppercase
    async def post(self, request):
        return text("test post")
