from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager =LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    #Configuracion de Login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Inicia sesion para continuar'
    login_manager.login_message_category = 'warning'

    #Modelos
    from app.models import Usuario
    from app.models import Categoria
    from app.models import Producto        
    from app.models import Pedido, DetallePedido 

    #User loader; Flask-login necesita saber como cargar un usuario por ID
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))


    # Blueprints
    from app.blueprints.public import public_bp
    from app.blueprints.auth import auth_bp
    from app.blueprints.admin import admin_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app