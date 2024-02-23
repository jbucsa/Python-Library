from flask import Flask
from flask_migrate import Migrate 

# Factory 
          
def create_app():
    app = Flask(__name__)
           
    # database config 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/Pet-Fax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from . import models 
    models.db.init_app(app) 
    migrate = Migrate(app, models.db)


    @app.route('/')
    def hello():
        return 'Hello!'
    
    #register blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    return app