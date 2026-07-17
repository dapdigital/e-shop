from flask import render_template, redirect, url_for, flash, request
from . import admin_bp
from flask_login import login_required
from .decorators import admin_requerido
from app import db
from app.models import Categoria
from .forms import FormCategoria


@admin_bp.route('/dashboard')
@login_required
@admin_requerido
def dashboard():
    return render_template('admin/home.html')


@admin_bp.route('/admin/productos')
def productos():
    return render_template('admin/productos.html')


@admin_bp.route('/admin/clientes')
def clientes():
    return render_template('admin/clientes.html')


@admin_bp.route('/admin/pedidos')
def pedidos():
    return render_template('admin/pedidos.html')


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