from flask import Flask
from app.extensions import db, migrate, jwt
from flask_bcrypt import Bcrypt

# Initialize Bcrypt outside the create_app function
bcrypt = Bcrypt()

from app.controllers.auth.auth_controller import auth
from app.controllers.authors.authors_controller import authors
from app.controllers.companies.companies_controller import companys
from app.controllers.books.books_controller import books

def create_app():
    # Application factory function
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
# Import models 
    from app.models.authors import Author
    from app.models.books import Book
    from app.models.companies import Company

    # Register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(authors)
    app.register_blueprint(companys)
    app.register_blueprint(books)

    # Home route
    @app.route("/")
    def home():
        return "Authors API"

    return app