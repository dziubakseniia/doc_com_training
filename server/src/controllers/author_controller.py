from utils import db_session
from src.models.models import Book, Author

class AuthorController:
    async def get_all_authors(self, app):
        with db_session(app) as db:
            all_authors = db.query(Author).all()
            if all_authors:
                return all_authors
            return "There is no authors"
