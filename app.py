from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas
from database import engine, SessionLocal, init_db

from fastapi.middleware.cors import CORSMiddleware

init_db()

app = FastAPI(docs_url="/docs", redoc_url="/redoc", title="API Almacén")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/almacen/productos", response_model=list[schemas.ProductoOut])
def get_productos(db: Session = Depends(get_db)):
    return db.query(models.Producto).all()

@app.get("/almacen/productos/{producto_id}", response_model=schemas.ProductoOut)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).get(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

@app.post("/almacen/productos", response_model=schemas.ProductoOut)
def create_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    nuevo = models.Producto(**producto.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.put("/almacen/productos/{producto_id}", response_model=schemas.ProductoOut)
def update_producto(producto_id: int, producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = db.query(models.Producto).get(producto_id)
    if not db_producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.delete("/almacen/productos/{producto_id}")
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).get(producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    db.delete(producto)
    db.commit()
    return {"ok": True}
