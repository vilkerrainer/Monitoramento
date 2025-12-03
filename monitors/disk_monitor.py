import psutil


def get_disk_usage(path='/'):
    """Retorna informações sobre uso do disco"""
    disco = psutil.disk_usage(path)
    return {
        'percent': disco.percent,
        'used': disco.used,
        'total': disco.total
    }