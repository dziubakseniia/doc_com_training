from utils import db_session
from src.models.models import Book, Author

class BookController:
    async def get_all_books(self, app, request):
        with db_session(app) as db:
            last_name = request.args.get('author_last_name')
            if last_name:
                books = db.query(Book).join(Book.authors).filter(Author.last_name.contains(last_name)).all()
                return books
            else:
                all_books = db.query(Book).all()
                if all_books:
                    return all_books
            return "There is no books"
    
    async def create_new_book(self, app, request):
        with db_session(app) as db:
            json = request.json
            if json:
                book = Book(name=json.get('name'))
                author = Author(last_name=json.get('author_name'))
                book.authors.append(author)
                db.add(book)
                db.commit()
                return {"message": "Book was added successfully"}
