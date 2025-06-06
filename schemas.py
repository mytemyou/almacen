from pydantic import BaseModel, Field
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str]
    precio: float = Field(..., gt=0.0)
    stock: int = Field(..., ge=0)
    categoria: Optional[str]

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True
