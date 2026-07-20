import os
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for, flash, request, current_app
from . import admin_bp
from flask_login import login_required
from .decorators import admin_requerido
from app import db
from app.models import Categoria, Usuario, Pedido, Producto
from .forms import FormCategoria, FormProducto


@admin_bp.route('/dashboard')
@login_required
@admin_requerido
def dashboard():
    return render_template('admin/home.html')


# ==================== CATEGORÍAS ====================

@admin_bp.route('/categorias')
@login_required
@admin_requerido
def listar_categorias():
    categorias = Categoria.query.order_by(Categoria.nombre).all()
    return render_template('admin/categorias/listar.html', categorias=categorias)


@admin_bp.route('/categorias/crear', methods=['GET', 'POST'])
@login_required
@admin_requerido
def crear_categoria():
    form = FormCategoria()

    if form.validate_on_submit():
        nueva = Categoria(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            activa=True
        )
        db.session.add(nueva)
        db.session.commit()
        flash('Categoría creada correctamente.', 'success')
        return redirect(url_for('admin.listar_categorias'))

    return render_template('admin/categorias/formulario.html', form=form, titulo='Nueva categoría')


@admin_bp.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_requerido
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    form = FormCategoria(obj=categoria)

    if form.validate_on_submit():
        categoria.nombre = form.nombre.data
        categoria.descripcion = form.descripcion.data
        categoria.activa = form.activa.data
        db.session.commit()
        flash('Categoría actualizada correctamente.', 'success')
        return redirect(url_for('admin.listar_categorias'))

    return render_template('admin/categorias/formulario.html', form=form, titulo='Editar categoría')


@admin_bp.route('/categorias/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_requerido
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    categoria.activa = False
    db.session.commit()
    flash('Categoría desactivada.', 'warning')
    return redirect(url_for('admin.listar_categorias'))


# ==================== CLIENTES ====================

@admin_bp.route('/gestion-clientes')
@login_required
@admin_requerido
def gestion_clientes():
    clientes = Usuario.query.filter_by(rol='cliente').order_by(Usuario.nombre).all()
    return render_template('admin/clientes/listar.html', clientes=clientes)


@admin_bp.route('/gestion-clientes/toggle/<int:id>', methods=['POST'])
@login_required
@admin_requerido
def toggle_cliente(id):
    cliente = Usuario.query.get_or_404(id)
    cliente.activo = not cliente.activo
    db.session.commit()
    estado = 'activado' if cliente.activo else 'desactivado'
    flash(f'Cliente {estado} correctamente.', 'success')
    return redirect(url_for('admin.gestion_clientes'))


# ==================== PEDIDOS ====================

@admin_bp.route('/gestion-pedidos')
@login_required
@admin_requerido
def gestion_pedidos():
    pedidos = Pedido.query.order_by(Pedido.fecha.desc()).all()
    return render_template('admin/pedidos/listar.html', pedidos=pedidos)


@admin_bp.route('/gestion-pedidos/estado/<int:id>', methods=['POST'])
@login_required
@admin_requerido
def cambiar_estado_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    orden_estados = ['pendiente', 'pagado', 'enviado', 'entregado']

    if pedido.estado in orden_estados:
        idx = orden_estados.index(pedido.estado)
        if idx < len(orden_estados) - 1:
            pedido.estado = orden_estados[idx + 1]
            db.session.commit()
            flash(f'Pedido actualizado a "{pedido.estado}".', 'success')
        else:
            flash('El pedido ya está en el último estado.', 'info')

    return redirect(url_for('admin.gestion_pedidos'))


# ==================== PRODUCTOS ====================

@admin_bp.route('/productos')
@login_required
@admin_requerido
def productos():
    lista = Producto.query.order_by(Producto.nombre).all()
    return render_template('admin/productos/listar.html', productos=lista)


@admin_bp.route('/productos/crear', methods=['GET', 'POST'])
@login_required
@admin_requerido
def crear_producto():
    form = FormProducto()
    form.categoria_id.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(activa=True).all()]

    if form.validate_on_submit():
        nombre_archivo = None

        if form.imagen.data:
            archivo = form.imagen.data
            nombre_archivo = secure_filename(archivo.filename)
            ruta_guardado = os.path.join(current_app.root_path, 'static', 'img', nombre_archivo)
            archivo.save(ruta_guardado)

        nuevo = Producto(
            nombre=form.nombre.data,
            descripcion=form.descripcion.data,
            precio=form.precio.data,
            stock=form.stock.data,
            categoria_id=form.categoria_id.data,
            imagen=nombre_archivo,
            activo=True
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Producto creado correctamente.', 'success')
        return redirect(url_for('admin.productos'))

    return render_template('admin/productos/formulario.html', form=form, titulo='Nuevo producto')


@admin_bp.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_requerido
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    form = FormProducto(obj=producto)
    form.categoria_id.choices = [(c.id, c.nombre) for c in Categoria.query.filter_by(activa=True).all()]

    if form.validate_on_submit():
        if form.imagen.data:
            archivo = form.imagen.data
            nombre_archivo = secure_filename(archivo.filename)
            ruta_guardado = os.path.join(current_app.root_path, 'static', 'img', nombre_archivo)
            archivo.save(ruta_guardado)
            producto.imagen = nombre_archivo

        producto.nombre = form.nombre.data
        producto.descripcion = form.descripcion.data
        producto.precio = form.precio.data
        producto.stock = form.stock.data
        producto.categoria_id = form.categoria_id.data
        producto.activo = form.activo.data
        db.session.commit()
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('admin.productos'))

    return render_template('admin/productos/formulario.html', form=form, titulo='Editar producto')


@admin_bp.route('/productos/eliminar/<int:id>', methods=['POST'])
@login_required
@admin_requerido
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    producto.activo = False
    db.session.commit()
    flash('Producto desactivado.', 'warning')
    return redirect(url_for('admin.productos'))