from flask import Flask
from app.extensions import db, migrate, jwt
from app.controllers.auth.auth_controller import auth
from app.controllers.authors.authors_controller import authors


#application factory function.
def create_app():
     
     #app instance
     app =  Flask(__name__)
     app.config.from_object('config.Config')  #Configuration comes fast.
     
     db.init_app(app) # initialise the db second
     migrate.init_app(app, db) # then u migrate
     jwt.init_app(app)
    
     
     
     
     # Importing and registering models
     
     from app.models.authors import Author
     from app.models.companies import Company
     from app.models.books import Book

     #registering blueprints
     app.register_blueprint(auth)
     app.register_blueprint(authors)
     
     
     @app.route("/")
     def home(app):       #Initializing out database instance on our app variable
          return "Authors API Project"


     return app


if __name__ == '__main__':
   create_app.run()
   