from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return '!!Hola!! Mi PetFax'
    
    # This was originally ('/pets') before we created the pet.py file and the [from . import pet] route
    @app.route('/Unknown')
    def Unknown() :
        return 'These are all the Flask Pet available for adoption. Limited Supply!!!!!'
    
    # Register Pet Blueprint
    from . import pet
    app.register_blueprint(pet.bp)


    # Return the app
    return app