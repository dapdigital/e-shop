from app import create_app, db
from app.models import Usuario

app = create_app()

with app.app_context():
    # Usuarios
    admin = Usuario(nombre='Administrador', email='admin@tienda.com', rol='admin')
    admin.set_password('admin123')

    cliente = Usuario(nombre='Juan Pérez', email='juan@email.com', rol='cliente')
    cliente.set_password('cliente123')

    db.session.add_all([admin, cliente])
    db.session.commit()

    print("✅ Datos de prueba insertados correctamente")