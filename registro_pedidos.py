from fastapi import HTTPException
from modelos import Pedido
import datetime

# Simular almacenamiento en memoria (para esta prueba)
pedidos_entregados = []

# Función para registrar pedidos
def registrar_pedido(pedido: Pedido):
    # Simulación de validación de tiempo (10 segundos)
    tiempo_actual = datetime.datetime.now()
    diferencia = tiempo_actual - pedido.timestamp
    if diferencia.total_seconds() > 10:
        raise HTTPException(status_code=400, detail="Entrega fuera de tiempo permitido")

    # Guardar el pedido en una lista (simula almacenamiento)
    pedidos_entregados.append(pedido.dict())
    return {"mensaje": "Pedido registrado correctamente", "pedido": pedido.dict()}

# Función para obtener todos los pedidos
def obtener_todos_los_pedidos():
    return pedidos_entregados
