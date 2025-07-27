import psutil


def info_memory():
    memory = psutil.virtual_memory()

    total_gb = memory.total / (1024 ** 3)
    used_gb = memory.used / (1024 ** 3)
    available_gb = memory.available / (1024 ** 3)
    percent_used = memory.percent

    print(f'Memória total: {total_gb:.1f} GB')
    print(f'Memória usada: {used_gb:.1f} GB')
    print(f'Memória disponível: {available_gb:.1f} GB')
    print(f'Porcentagem em uso: {percent_used:.1f}%')


if __name__ == "__main__":
    info_memory()
