from app import create_app, db
from app.models import Categoria, Producto

app = create_app()

with app.app_context():
    for c in Categoria.query.all():
        n_productos = Producto.query.filter_by(categoria_id=c.id, activo=True).count()
        print(c.id, c.nombre, "activa=", c.activa, "| productos:", n_productos)