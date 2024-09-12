from registro_pedidos import pedidos_entregados
from datetime import datetime


# Métrica: Entregas por repartidor
def entregas_por_repartidor():
    metricas = {}
    for pedido in pedidos_entregados:
        repartidor = pedido['repartidor']
        if repartidor not in metricas:
            metricas[repartidor] = 0
        metricas[repartidor] += 1
    return metricas

# Métrica: Productos más vendidos
def productos_mas_vendidos():
    productos_count = {}
    for pedido in pedidos_entregados:
        for producto in pedido['productos']:
            producto_nombre = producto['producto']
            if producto_nombre not in productos_count:
                productos_count[producto_nombre] = 0
            productos_count[producto_nombre] += 1
    return productos_count


def entregas_recientes(horas: int = 24):
    ahora = datetime.now()
    recientes = []
    
    for pedido in pedidos_entregados:
        timestamp = pedido['timestamp']
        
        # Verifica si el timestamp es una cadena o un objeto datetime
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        
        if (ahora - timestamp).total_seconds() <= horas * 3600:
            recientes.append(pedido)

    return {"total_entregas": len(recientes), "entregas": recientes}
