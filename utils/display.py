import os


def clear_screen():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')


def hide_cursor():
    """Esconde o cursor do terminal"""
    print('\033[?25l', end='')


def show_cursor():
    """Mostra o cursor do terminal"""
    print('\033[?25h', end='')


def move_cursor_home():
    """Move o cursor para o início da tela"""
    print('\033[H', end='')


def display_system_info(cpu, memory, disk, temps):
    """Exibe as informações do sistema formatadas"""
    move_cursor_home()
    
    print("=== Monitor de Recursos do Sistema ===\n")
    print(f"Uso da CPU: {cpu}%      ")
    print(f"Uso de Memória: {memory['percent']}%      ")
    print(f"Uso do Disco: {disk['percent']}%      ")
    
    if isinstance(temps, dict):
        for hardware, temp in temps.items():
            print(f"Temperatura {hardware}: {temp}°C      ")
    else:
        print(f"Temperatura: {temps}      ")
    
    print("\nPressione Ctrl+C para sair      ")