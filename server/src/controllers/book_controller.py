from src.models.models import Book, Author
from utils import db_session


class BookController:
    async def get_all_books(self, app, request):
        with db_session(app) as db:
            last_name = request.args.get('author_last_name')
            if last_name:
                books = db.query(Book).join(Book.authors).filter(Author.last_name.contains(last_name)).all()
            else:
                books = db.query(Book).all()
            return books if books else "There is no books"
    
    async def create_new_book(self, app, request):
        with db_session(app) as db:
            json = request.json
            if json:
                book = Book(name=json.get('name'))
                last_name = json.get('author_name')
                author = db.query(Author).filter(Author.last_name == last_name).first()
                if author is None:
                    author = Author(last_name=last_name)
                book.authors.append(author)
                db.add(book)
                db.commit()
                return {"message": "Book was added successfully"}
