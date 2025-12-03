import psutil


def get_memory_usage():
    """Retorna informações sobre uso de memória"""
    memoria = psutil.virtual_memory()
    return {
        'percent': memoria.percent,
        'used': memoria.used,
        'total': memoria.total
    }