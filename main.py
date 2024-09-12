from fastapi import FastAPI, Depends
from modelos import Pedido
from registro_pedidos import registrar_pedido, obtener_todos_los_pedidos
from metricas import entregas_por_repartidor, productos_mas_vendidos, entregas_recientes
from auth import get_current_user  # Importar el sistema de autenticación

app = FastAPI()

# Endpoint para registrar pedidos (público)
@app.post("/registrar_pedido_entregado")
async def registrar_pedido_entregado(pedido: Pedido):
    return registrar_pedido(pedido)

# Endpoint para obtener todos los pedidos (público)
@app.get("/pedidos")
async def obtener_pedidos():
    return obtener_todos_los_pedidos()

# Endpoint para monitoreo: Entregas por repartidor (requiere autenticación)
@app.get("/metricas/entregas_por_repartidor")
async def metricas_entregas_por_repartidor(current_user: str = Depends(get_current_user)):
    return entregas_por_repartidor()

# Endpoint para monitoreo: Productos más vendidos (requiere autenticación)
@app.get("/metricas/productos_mas_vendidos")
async def metricas_productos_mas_vendidos(current_user: str = Depends(get_current_user)):
    return productos_mas_vendidos()

# Endpoint para monitoreo: Entregas recientes (requiere autenticación)
@app.get("/metricas/entregas_recientes")
async def metricas_entregas_recientes(horas: int = 24, current_user: str = Depends(get_current_user)):
    return entregas_recientes(horas)
