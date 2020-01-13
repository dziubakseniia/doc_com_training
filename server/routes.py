from views.author_view import AuthorView
from views.book_view import BookView
from views.test_status import TestStatusView
from views.redis_view import RedisView


def setup_routes(app):
    app.add_route(TestStatusView.as_view(), '/test')
    app.add_route(BookView.as_view(), '/books')
    app.add_route(AuthorView.as_view(), '/authors')
    app.add_route(RedisView.as_view(), '/redis')
