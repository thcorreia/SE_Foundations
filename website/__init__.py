from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
#from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "NaoAguentoMais2022!"  #SECURE AND ENCRIPT THE DATA SECRET KEY TO OUR APP
    app.config.from_object('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

 
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #from .models import User, Notes
    
    
    return app



 