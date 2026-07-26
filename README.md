# E-Shop

Tienda en línea de ropa llamada Dissonance, desarrollada con Flask como
proyecto académico. Incluye gestión de usuarios, categorías, productos y
pedidos, con un panel de administración.

## Integrantes
- [Diana Alvarado]
- [Amelia Bozano]
- [Estefania Simbaña]

## Requisitos previos
- Python 3.10 o superior
- pip  
- Git 
- MySQL / MariaDB, corriendo local mente

## Tecnologías
- Python3 + Flask
- Flask-SQLAlchemy + Flask-Migrate (ORM y migraciones de base de datos)
- Flask-Login (autenticación) · Flask-WTF (formularios y validación de archivo)
- MySQL / MariaDB 
- Bootstrap 5 + CSS propio

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/dapdigital/e-shop.git
cd e-shop
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

# En Windows (PowerShell):
.venv\Scripts\Activate.ps1

# En Windows (Git Bash):
source .venv/Scripts/activate

# En Linux/Mac:
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto con:
```
FLASK_ENV=development
SECRET_KEY=tu-clave-secreta
DB_USER=root
DB_PASSWORD=
DB_HOST=localhost
DB_NAME=ecommerce_db
```
### 5. Crear Base de Datos
   ```sql
   CREATE DATABASE ecommerce_db;
   CREATE USER 'ecommerce_user'@'localhost' IDENTIFIED BY '123456';
   GRANT ALL PRIVILEGES ON ecommerce_db.* TO 'ecommerce_user'@'localhost';
   FLUSH PRIVILEGES;
   ```
### 6. Aplicar las migraciones
```bash
set FLASK_APP=run.py # En Linux/Mac: export FLASK_APP=run.py
flask db upgrade
```
### 7. Cargar usuarios de prueba
```bash
python seed.py
```
### 8. Ejecutar el proyecto
```bash
python run.py
```
La aplicación estará disponible en `http://127.0.0.1:5000`

## Usuarios de prueba (seed)
- **Admin:** admin@tienda.com / admin123
- **Cliente:** juan@email.com / cliente123 

## Estructura del proyecto
```
e-shop/
├── .gitignore
├── app.py
├── run.py
├── seed.py
├── borrar_categorias.py
├── README.md
├── requirements.txt
├── .env.example
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── data_productos.py        # catálogo fuente (categorías + productos)
│   ├── blueprints/
│   │   ├── public/              # tienda, acerca de, contacto
│   │   ├── auth/                # login / registro
│   │   └── admin/                # panel de administración
│   ├── models/                  # Usuario, Categoria, Producto, Pedido...
│   ├── utils/
│   │   └── importar_excel.py    # sincronización automática del catálogo
│   ├── static/
│   │   ├── css/style.css
│   │   └── img/                 # imágenes de productos
│   └── templates/
└── migrations/
    ├── alembic.ini
    ├── env.py
    └── versions/
```
## Rutina diaria (después de la primera instalación)
```bash
git pull
pip install -r requirements.txt
flask db upgrade
python run.py
 ```