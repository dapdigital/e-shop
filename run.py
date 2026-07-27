from app import create_app

app = create_app()

if __name__ == '__main__':
    # app.debug ya viene de Config.DEBUG (según FLASK_ENV en el .env).
    # Esto es solo para desarrollo local; en el servidor se usa gunicorn
    # (ver wsgi.py), que no pasa por este bloque.
    app.run(debug=app.debug)