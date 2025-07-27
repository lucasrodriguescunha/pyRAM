import psutil


def info_memory():
    memory = psutil.virtual_memory()
    print(f'Memória total: {memory.total / (1024 ** 3):.1f} GB')
    print(f'Memória usada: {memory.used / (1024 ** 3):.1f} GB')
    print(f'Memória disponível: {memory.available / (1024 ** 3):.1f} GB')
    print(f'Porcentagem em uso: {memory.percent:.1f}%')


if __name__ == "__main__":
    info_memory()
