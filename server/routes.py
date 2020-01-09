from views.test_status import TestStatusView
from views.book_view import BookView
from views.author_view import AuthorView

def setup_routes(app):
    app.add_route(TestStatusView.as_view(), '/test')
    app.add_route(BookView.as_view(), '/books')
    app.add_route(AuthorView.as_view(), '/authors')
