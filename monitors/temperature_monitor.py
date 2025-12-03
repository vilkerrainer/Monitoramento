import platform
import psutil
import wmi


def get_temperatures():
    """Retorna as temperaturas do sistema"""
    so = platform.system()

    if so == "Linux":
        temps = psutil.sensors_temperatures()
        return temps

    if so == "Windows":
        try:
            w = wmi.WMI(namespace="root\\LibreHardwareMonitor")
            sensors = w.Sensor()
            
            temps = {}
            for sensor in sensors:
                if sensor.SensorType == 'Temperature':
                    if 'Tctl' in sensor.Name or 'Tdie' in sensor.Name:
                        temps['CPU'] = round(sensor.Value, 1)
                    elif 'GPU Core' in sensor.Name:
                        temps['GPU'] = round(sensor.Value, 1)
            
            return temps if temps else "LibreHardwareMonitor não está rodando"
        except:
            return "Erro: Execute o LibreHardwareMonitor como administrador"

    return None