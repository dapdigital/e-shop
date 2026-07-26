"""
Sincroniza productos desde app/data_productos.py cada vez que arranca
la aplicación (python run.py / flask run).

Por cada producto de la lista PRODUCTOS:
  - crea la categoría si no existe
  - crea el producto si no existe (busca por nombre)
  - si el producto ya existe, actualiza precio, stock, descripcion e imagen

Es seguro que corra en cada arranque: no duplica nada, solo actualiza lo que cambió.
"""
import os


def sincronizar_productos_desde_excel(app, db):
    try:
        from app.data_productos import PRODUCTOS
        from app.models import Categoria, Producto
    except Exception as e:
        print(f'[sincronizar_productos] No se pudo importar el catálogo: {e}')
        return

    carpeta_imagenes = os.path.join(app.root_path, 'static', 'img')

    try:
        creadas_categorias = 0
        creados = 0
        actualizados = 0
        imagenes_faltantes = []

        for p in PRODUCTOS:
            categoria_nombre = p.get('categoria')
            nombre = p.get('nombre')
            descripcion = p.get('descripcion')
            precio = p.get('precio')
            stock = p.get('stock')
            imagen = p.get('imagen')

            if not nombre or precio is None:
                continue

            categoria = Categoria.query.filter(
                db.func.lower(Categoria.nombre) == str(categoria_nombre).strip().lower()
            ).first()
            if not categoria:
                categoria = Categoria(nombre=str(categoria_nombre).strip(), activa=True)
                db.session.add(categoria)
                db.session.flush()
                creadas_categorias += 1

            if imagen and not os.path.exists(os.path.join(carpeta_imagenes, imagen)):
                imagenes_faltantes.append(imagen)

            producto = Producto.query.filter(
                db.func.lower(Producto.nombre) == str(nombre).strip().lower()
            ).first()

            if producto:
                producto.descripcion  = descripcion
                producto.precio       = precio
                producto.stock        = int(stock or 0)
                producto.imagen       = imagen
                producto.categoria_id = categoria.id
                producto.activo       = True
                actualizados += 1
            else:
                db.session.add(Producto(
                    nombre=str(nombre).strip(),
                    descripcion=descripcion,
                    precio=precio,
                    stock=int(stock or 0),
                    imagen=imagen,
                    categoria_id=categoria.id,
                    activo=True
                ))
                creados += 1

        db.session.commit()
        print(f'[sincronizar_productos] Categorías nuevas: {creadas_categorias} | '
              f'Productos creados: {creados} | Actualizados: {actualizados}')
        if imagenes_faltantes:
            print(f'[sincronizar_productos] ⚠️ {len(imagenes_faltantes)} imagen(es) '
                  f'no están en app/static/img/: {sorted(set(imagenes_faltantes))}')

    except Exception as e:
        db.session.rollback()
        print(f'[sincronizar_productos] ⚠️ No se pudo sincronizar (¿ya corriste las '
              f'migraciones? ¿la base de datos está arriba?): {e}')