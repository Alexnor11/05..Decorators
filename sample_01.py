# *args **kwargs


def foo(*args, **kwargs):
    print('args', args)  # Не именнованные аргументы
    print('kwargs', kwargs)  # Именнованые аргументы


foo(1, 5, 8, 7, b='5', d=None)  # Добавляем любое количество аргументов


