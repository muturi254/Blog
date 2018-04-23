
from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])


    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    # secure user cookies when logged in
    

    # register blueprints
        # main blue print
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
        # auth blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
        # blog blue print
    from . Blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app
