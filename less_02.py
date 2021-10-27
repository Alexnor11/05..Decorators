import webbrowser


# декоратор проверяет на верный url:
def validator(func):
    def wrapper(url):
        if '.' in url:
            func(url)
        else:
            print('Неверный URL')
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)


open_url("https://bikexp")