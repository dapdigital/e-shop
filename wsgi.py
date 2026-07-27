"""
Punto de entrada para gunicorn (servidor de producción).

En el servidor se corre con:
    gunicorn wsgi:app --bind 0.0.0.0:8000

"python run.py" sigue siendo solo para desarrollo local.
"""
from app import create_app

app = create_app()