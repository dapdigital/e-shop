"""
Script de un solo uso: borra permanentemente las categorías
Electrónica, Hogar y Ropa, junto con sus productos.

Como son datos de PRUEBA, también borra los detalles de pedido
que hagan referencia a esos productos (no borra el pedido completo,
solo la línea de ese producto dentro del pedido).

Uso:
    python borrar_categorias.py
"""
from app import create_app, db
from app.models import Categoria, Producto, DetallePedido, Pedido

app = create_app()

NOMBRES_A_BORRAR = ['electronica', 'electrónica', 'hogar', 'ropa']

with app.app_context():
    categorias = Categoria.query.filter(
        db.func.lower(Categoria.nombre).in_(NOMBRES_A_BORRAR)
    ).all()

    if not categorias:
        print('No se encontró ninguna categoría con esos nombres. Nada que borrar.')
    else:
        for categoria in categorias:
            productos = Producto.query.filter_by(categoria_id=categoria.id).all()
            print(f'\nCategoría "{categoria.nombre}" ({len(productos)} productos)')

            for producto in productos:
                detalles = DetallePedido.query.filter_by(producto_id=producto.id).all()

                if detalles:
                    print(f'  🗑 Borrando {len(detalles)} línea(s) de pedido de prueba '
                          f'de "{producto.nombre}"')
                    for d in detalles:
                        db.session.delete(d)
                    db.session.flush()

                print(f'  ✔ Eliminando producto "{producto.nombre}"')
                db.session.delete(producto)

            db.session.flush()

            print(f'  ✔ Eliminando categoría "{categoria.nombre}"')
            db.session.delete(categoria)

        db.session.commit()
        print('\nListo.')