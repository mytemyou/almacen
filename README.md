# 🧺 Microservicio Almacén

API RESTful desarrollada con **FastAPI**, que permite gestionar un catálogo de productos (CRUD completo). Este microservicio forma parte de una arquitectura contenerizada y está listo para ejecutarse con Docker y Docker Compose.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3.10

---

## 🧪 Endpoints disponibles

```http
GET    /almacen/productos         → Obtener todos los productos  
GET    /almacen/productos/{id}    → Obtener un producto por ID  
POST   /almacen/productos         → Crear un nuevo producto  
PUT    /almacen/productos/{id}    → Actualizar un producto existente  
DELETE /almacen/productos/{id}    → Eliminar un producto  
```

### 📦 Esquema de producto (JSON)

Este es el formato que debe tener un producto al enviarlo por `POST` o `PUT`:

```json
{
  "nombre": "Auriculares Bluetooth",
  "descripcion": "Cancelación de ruido y batería de larga duración",
  "precio": 59.99,
  "stock": 120,
  "categoria": "Electrónica"
}
```

---

## ▶️ Instrucciones de uso

### 🐳 Ejecutar con Docker Compose

```bash
docker-compose up --build
```

La API estará disponible en:  
[http://localhost:1234](http://localhost:1234)

Documentación Swagger automática en esa URL raíz.

### 🔧 Detener contenedores

```bash
docker-compose down
```

---

## 📁 Estructura del proyecto

```
almacen/
├── app.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .gitignore
```

---

## 📌 Notas

- Base de datos local SQLite (puede sustituirse por PostgreSQL fácilmente).
- El código está preparado para producción en contenedores.
- Incluye middleware CORS para facilitar pruebas desde cualquier cliente.

---

## ✍️ Autor

- Miguel Hernández Barrionuevo  
  Estudiante de Máster Big Data & Data Engineering  
  [LinkedIn](https://linkedin.com) *(opcional)*