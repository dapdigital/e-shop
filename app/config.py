import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")

    # DB_PORT tiene 3306 por defecto (MySQL local), pero Railway asigna
    # un puerto distinto para su MySQL en la nube, asi que se puede
    # sobreescribir con la variable DB_PORT.
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT', '3306')}/{os.getenv('DB_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DEBUG se apaga automaticamente cuando FLASK_ENV=production
    DEBUG = os.getenv("FLASK_ENV", "development") != "production"
