from app.extensions import db
from datetime import datetime

class Company(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(100), nullable = False, unique = True)
    origin = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text(200), nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id")) #foreign key from the authors model
    author = db.relationship('Author', backref = 'companies')  #Relationship between the user and the company(this is basically a one to many relationship)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())
    
    
    def __init__ (self, name, origin, description, author_id):              
          super(Company, self).__init__()
          self.name = name   
          self.origin = origin           
          self.description = description
          self.author_id = author_id
          
    
    def __repr__(self):
        return f"{self.name} {self.origin}"
          
    
    
    