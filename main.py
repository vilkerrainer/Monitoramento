import time
from monitors.cpu_monitor import get_cpu_usage
from monitors.memory_monitor import get_memory_usage
from monitors.disk_monitor import get_disk_usage
from monitors.temperature_monitor import get_temperatures
from utils.display import (
    clear_screen,
    hide_cursor,
    show_cursor,
    display_system_info
)


def main():
    """Função principal do monitor de sistema"""
    clear_screen()
    hide_cursor()
    
    try:
        while True:
            cpu = get_cpu_usage(interval=0.5)
            memory = get_memory_usage()
            disk = get_disk_usage('/')
            temps = get_temperatures()
            
            display_system_info(cpu, memory, disk, temps)
            
            time.sleep(0.5)
    
    except KeyboardInterrupt:
        show_cursor()
        print("\n\nMonitor encerrado!")


if __name__ == "__main__":
    main()