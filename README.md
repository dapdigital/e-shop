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

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/dapdigital/e-shop.git
cd e-shop
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
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
### 5. Inicializar la base de datos
```bash
flask db upgrade
python seed.py
```

### 6. Ejecutar el proyecto
```bash
python run.py
```
La aplicación estará disponible en `http://127.0.0.1:5000`
 

## Estructura del proyecto
```
e-shop/
├── .gitignore
├── app.py
├── run.py
├── seed.py
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── blueprints/
│   ├── models/
│   ├── static/
│   └── templates/
└── migrations/
    ├── alembic.ini
    ├── env.py
    └── script.py.mako
```