# Декораторы:
import datetime


def add_logger(func):
    def wrapper(*args, **kwargs):
        with open('file/log.txt', 'a', encoding='utf-8') as log_file:
            logs = (f'Дата и время вызова функции: {datetime.datetime.now().strftime("%d %b %Y, %H:%M:%S")}\n'
                    f'Имя функции: {func.__name__}\n'
                    f'Аргументы:  {args} {kwargs} \n'
                    f'Возвращаемое значение: {func(*args, **kwargs)}\n{"---" * 8}\n')
            log_file.write(logs)
        result = func(*args, **kwargs)
        return result

    return wrapper


@add_logger
def get_foo(a, b, c=5, d=5):
    """Функция для теста"""
    res = (a + b) + c * d
    return res


foo = get_foo
print(foo(10, 8, c=15, d=10))
