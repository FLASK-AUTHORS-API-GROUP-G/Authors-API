from app.extensions import db
from datetime import datetime

class Author (db.Model):      # inherit from the model class
     __tablename__ = "authors"
     id = db.Column(db.Integer, primary_key=True, nullable = False)
     first_name = db.Column(db.String(20))
     last_name = db.Column(db.String(20))
     contact = db.Column(db.Integer, nullable = False, unique = True)
     email = db.Column(db.String(30), nullable = False, unique = True)
     password = db.Column(db.String(255), nullable = False)
     image = db.Column(db.String(100), nullable = True) 
     bio = db.Column(db.String(200))
     created_at = db.Column(db.DateTime, default= datetime.now())
     updated_at = db.Column(db.DateTime, onupdate = datetime.now())
     
     def __init__ (self, first_name, last_name, contact, email, password, bio, image=None):
          super(Author, self).__init__()
                         
          self.first_name = first_name   
          self.last_name = last_name
          self.email = email
          self.password = password           
          self.image= image
          self.bio= bio
          self.contact= contact
        

     def author_info(self):
       return  f" {self.first_name} {self.last_name}"