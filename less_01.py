import datetime
import webbrowser


# Демострация работы декоратора:
def validator(func):
    def wrapper(*args, **kwargs):
        print(f'Дата и время вызова функции: {datetime.datetime.now()}\n'
              f'Аргументы:  {args} {kwargs}\n'
              f'Имя функции: {func.__name__}')
        func(*args, **kwargs)
        # print('Это текст после функции')

    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


open_url("https://bikexp.ru")

