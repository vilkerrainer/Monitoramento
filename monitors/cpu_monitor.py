import psutil


def get_cpu_usage(interval=0.5):
    """Retorna o uso atual da CPU em porcentagem"""
    return psutil.cpu_percent(interval=interval)