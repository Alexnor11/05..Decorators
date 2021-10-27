# Декораторы:
import datetime
import os


def parametrized_decor(path_file):
    def add_logger(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path_file, 'a', encoding='utf-8') as log_file:
                logs = (f'Дата и время вызова функции: {datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S")}\n'
                        f'Имя функции: {func.__name__}\n'
                        f'Аргументы:  {args} {kwargs} \n'
                        f'Возвращаемое значение: {func(*args, **kwargs)}\n'
                        # Обсалютный путь к файлу логов:
                        f'Путь к логам: {os.path.abspath(path_file)}\n{"---" * 8}\n')
                log_file.write(logs)

            return result
        return wrapper
    return add_logger


@parametrized_decor('file/log.txt')
def get_foo(a, b, c=5, d=5):
    """Функция для теста"""
    res = (a + b) + c * d
    return res


foo = get_foo
print(foo(5, 25, c=12, d=100))
