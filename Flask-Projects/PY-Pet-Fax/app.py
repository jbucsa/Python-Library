# config                    
# from flask import Flask 
# app = Flask(__name__)

# # Index Route
# @app.route('/')
# def index():
#     return 'Hello and welcome to Flask App!!!!'

# #Pets Index Routes
# @app.route('/pets')
# def pets() :
#     return 'These are all the Flask Pet available for adoption. Limited Supply!!!!!'


from petfax import create_app
app =  create_app()
