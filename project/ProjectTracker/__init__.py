from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

#import FoamToolTracker2020.views

#from flask import Flask
#app = Flask(__name__)

def create_app(HOST, PORT):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

       # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    #from .views import views as views_blueprint
    #app.register_blueprint(views_blueprint)

    #app.debug = True


    app.run(HOST, PORT)

    return app

