from pydantic import BaseModel
from typing import List
import datetime

# Definición del modelo Producto
class Producto(BaseModel):
    IdProducto: str
    producto: str
    precio: float

# Definición del modelo Pedido
class Pedido(BaseModel):
    pedido_id: str
    repartidor: str
    productos: List[Producto]
    timestamp: datetime.datetime
