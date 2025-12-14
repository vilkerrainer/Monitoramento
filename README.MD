# Monitor de Recursos do Sistema

Monitor em tempo real de CPU, memória, disco e temperatura do sistema para Windows e Linux.

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Windows
- **LibreHardwareMonitor** (para leitura de temperatura)
  - Download: [LibreHardwareMonitor Releases](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases)
  - Extraia e execute `LibreHardwareMonitor.exe` **como Administrador**

### Linux
- Sensores de temperatura configurados (geralmente já vem por padrão)

## Instalação

### 1. Clone ou baixe o projeto

```bash
git clone https://github.com/vilkerrainer/Monitoramento.git
cd monitoramento
```

### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Como Usar

### Windows

1. **Execute o LibreHardwareMonitor como Administrador**
   - Abra o `LibreHardwareMonitor.exe` que você baixou
   - Clique com botão direito → "Executar como Administrador"
   - Minimize (deixe rodando em segundo plano)

2. **Execute o monitor**
   ```bash
   python main.py
   ```

### Linux

```bash
python3 main.py
```

## O que é monitorado

- **CPU**: Uso em porcentagem
- **Memória RAM**: Uso em porcentagem
- **Disco**: Uso em porcentagem
- **Temperatura**: CPU e GPU (quando disponível)

## Para Encerrar

Pressione `Ctrl+C` no terminal para sair do monitor.

## Estrutura do Projeto

```
monitoramento/
├── main.py                      # Arquivo principal
├── monitors/                    # Módulos de monitoramento
│   ├── __init__.py
│   ├── cpu_monitor.py          # Monitor de CPU
│   ├── memory_monitor.py       # Monitor de Memória
│   ├── disk_monitor.py         # Monitor de Disco
│   └── temperature_monitor.py  # Monitor de Temperatura
├── utils/                       # Utilitários
│   ├── __init__.py
│   └── display.py              # Funções de exibição
├── requirements.txt            # Dependências
└── README.md                   # Este arquivo
```

## Dependências

- `psutil` - Monitoramento de recursos do sistema
- `wmi` - Acesso ao WMI do Windows (apenas Windows)
- `pywin32` - Dependência do wmi (apenas Windows)

## Solução de Problemas

### Windows: "Erro: Execute o LibreHardwareMonitor como administrador"

**Solução:** Certifique-se de que o LibreHardwareMonitor está rodando com privilégios de administrador.

### Windows: "LibreHardwareMonitor não está rodando"

**Solução:** Abra o LibreHardwareMonitor e deixe-o em execução enquanto usa o monitor.

### Linux: Temperatura não aparece

**Solução:** Instale os sensores:
```bash
sudo apt-get install lm-sensors
sudo sensors-detect
```

## Licença

Este projeto é de código aberto e está disponível para uso livre.

## Autor

Desenvolvido para monitoramento eficiente do sistema.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
