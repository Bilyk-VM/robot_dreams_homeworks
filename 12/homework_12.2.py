# імпортуємо datetime
import json
from datetime import datetime

# створимо декоратор, який буде доповнювати функції їх назвою та часом виклику
def deco(func):
    def inner(*args, **kwargs):

        # запишемо потрібну інформацію в словник info: назву функції (ключ), та час її виклику (значення)
        info = {func.__name__: str(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))}

        # запишемо інформацію в файл f_info.txt, використовуючи атрибут "а" для дозапису даних
        with open('f_info.txt', 'a') as f:
            json.dump(info, f, indent=1)

        # викликаємо функцію, яка буде декоруватись
        res = func(*args, **kwargs)
        return res
    return inner

# задекоруємо декілька простих функцій
@deco
def first_func(val_1):
    print(f'This is the first function with value: {val_1}')

@deco
def second_func(val_2):
    print(f'This is the second function with value: {val_2}')

# викличем ці функції
first_func(5)
input()
second_func(10)

