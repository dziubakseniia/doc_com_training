from sanic.views import HTTPMethodView
from sanic.response import text

from src.controllers.author_controller import AuthorController

class AuthorView(HTTPMethodView):
    def __init__(self):
        self.authors = AuthorController()

    async def get(self, request):
        app = request.app
        lst = await self.authors.get_all_authors(app)
        return text(lst)
