import json

from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('book_id', Integer, ForeignKey('books.id')),
    Column('author_id', Integer, ForeignKey('authors.id'))
)


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=False)
    books = relationship(
        "Book",
        secondary=association_table,
        back_populates="authors",
    )

    def __repr__(self):
        return f"<Author(id={self.id}, first_name={self.first_name}, last_name={self.last_name})>"
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    authors = relationship(
        "Author",
        secondary=association_table,
        back_populates="books",
    )

    def __repr__(self):
        return f"<Book(id={self.id}, name={self.name})>"
