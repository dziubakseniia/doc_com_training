from src.models.models import Author
from utils import db_session


class AuthorController:
    async def get_all_authors(self, app):
        with db_session(app) as db:
            all_authors = db.query(Author).all()
            return all_authors if all_authors else "There is no authors"
