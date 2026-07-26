"""
Borra automáticamente, en cada arranque de la app, las categorías de
PRUEBA (Electrónica, Hogar, Ropa) y sus productos/detalles de pedido
asociados, si es que existen. Es el mismo comportamiento de
borrar_categorias.py, pero corriendo solo, para no depender de que
alguien lo ejecute a mano en el servidor.

Es seguro que corra en cada arranque: si ya no existen esas categorías,
simplemente no hace nada.
"""

NOMBRES_A_BORRAR = ['electronica', 'electrónica', 'hogar', 'ropa']


def eliminar_categorias_de_prueba(app, db):
    try:
        from app.models import Categoria, Producto, DetallePedido
    except Exception as e:
        print(f'[limpiar_categorias] No se pudo importar modelos: {e}')
        return

    try:
        categorias = Categoria.query.filter(
            db.func.lower(Categoria.nombre).in_(NOMBRES_A_BORRAR)
        ).all()

        if not categorias:
            return  # nada que limpiar

        total_productos = 0
        for categoria in categorias:
            productos = Producto.query.filter_by(categoria_id=categoria.id).all()
            for producto in productos:
                DetallePedido.query.filter_by(producto_id=producto.id).delete()
                db.session.delete(producto)
                total_productos += 1
            db.session.delete(categoria)

        db.session.commit()
        print(f'[limpiar_categorias] Categorías de prueba eliminadas: '
              f'{len(categorias)} (con {total_productos} producto(s))')

    except Exception as e:
        db.session.rollback()
        print(f'[limpiar_categorias] ⚠️ No se pudo limpiar: {e}')