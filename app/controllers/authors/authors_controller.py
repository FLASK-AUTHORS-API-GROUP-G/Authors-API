# storing all functions used for performing the different authentication process of log in and log out.
from flask import Blueprint, request, jsonify
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_401_UNAUTHORIZED,HTTP_200_OK
import validators 
from app.models.authors import Author
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity,create_refresh_token


#authors blueprint
authors = Blueprint('authors', __name__, url_prefix ='/api/v1/authors')


# Retrieving all authors from the database

@authors.get('/author')
@jwt_required()
def getAllAuthors():
    
    try:
        all_authors = Author.query.all()

        authors_data = []

        for author in all_authors:
             author_info = {
                 'id':author.id,
                 'first_name':author.first_name,
                 'last_name':author.last_name,
                 'author_name': author.author_info(),
                 'email':author.email,
                 'contact':author.contact,
                 'bio':author.bio,
                 'created_at':author.created_at,
                 'companies': [],
                 'books':[]
                 

             }

             if hasattr(author,'books'):
                 author_info['books'] = [{
                    'id':book.id,
                    'title':book.title,
                    'price':book.price,
                    'genre':book.genre,
                    'price_unit':book.price_unit,
                    'publication_date':book.publication_date,
                    'description':book.description,
                    'image':book.image,
                    'created_at':book.created_at,
                 } for book in author.books]


             if hasattr(author, 'companies'):
                 author_info['companies']=[{
                     'id':company.id,
                     'name':company.name,
                     'origin':company.origin,
                 } for company in author.companies]

             authors_data.append(author_info)


        return jsonify({
            "message": "All authors retrieved successfully",
            "total_authors":len(authors_data),
            "authors": authors_data
        }),HTTP_200_OK
                  



    except Exception as e:
        return jsonify({
            'error': str(e)
        }), HTTP_500_INTERNAL_SERVER_ERROR



