import psutil


def info_memory():
    memory = psutil.virtual_memory()

    total_gb = memory.total / (1024 ** 3)
    used_gb = memory.used / (1024 ** 3)
    available_gb = memory.available / (1024 ** 3)
    percent_used = memory.percent

    print(f'Memória total: ${total_gb} GB')
    print(f'Memória usada: ${used_gb} GB')
    print(f'Memória disponível: ${available_gb} GB')
    print(f'Porcentagem em uso: ${percent_used}%')


if __name__ == "__main__":
    info_memory()
