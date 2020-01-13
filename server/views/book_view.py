from sanic.response import text
from sanic.views import HTTPMethodView

from src.controllers.book_controller import BookController


class BookView(HTTPMethodView):
    def __init__(self):
        self.books = BookController()

    async def get(self, request):
        app = request.app
        lst = await self.books.get_all_books(app, request)
        return text(lst)

    async def post(self, request):
        app = request.app
        json = await self.books.create_new_book(app, request)
        return text(json)
