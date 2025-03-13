from app.extensions import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    title = db.Column(db.String(120), nullable = False)
    pages = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    price_unit = db.Column(db.String(35), nullable = False, default = "UGX")
    publication_date = db.Column(db.Date, nullable = False)
    isbn = db.Column(db.String(30), nullable = True, unique = True)
    genre = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(220), nullable = False)
    image = db.Column(db.String(120), nullable = True)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"))
    author = db.relationship('Author', backref = 'books') # backref property navigates us back to the parent class which is now the authors from 
    #the child class which is books. Meaning an author can publish one or more books
    company = db.relationship('Company', backref = 'books') # A company can ave many books.
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())
    
    
    
    def __init__ (self, title, price, description ,genre, pages, price_unit, publication_date, isbn, image, company_id, author_id ):              
          super(Book, self).__init__()
          self.title = title   
          self.price = price           
          self.description = description
          self.genre = genre
          self.pages = pages
          self.price_unit = price_unit
          self.publication_date = publication_date
          self.isbn = isbn
          self.image = image
          self.author_id = author_id
          self.company_id = company_id
          
    def __repr__(self):
        return f"Book {self.title}"
          
          
          
          
# Read about authentication and how it works
# Explain the aunthentication process
# Explain the purpose of blue prints.
# Organise/create routes for each model using the CRUD Approach with the help of http methods.
# have another table for methods and descriptions.
          
# deadline 10th marc 6pm
# deadline for groupwork submission is 5th and presentation is 13th
          
    