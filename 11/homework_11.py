# ==================== 11.1
# Написати декоратор
# імпортуємо datetime
from datetime import datetime

# створимо декоратор, який буде доповнювати функції їх назвою та часом виклику
def deco(func):
    def inner(*args, **kwargs):
        # виведем назву функції, за допомогою методу __name__
        print(f"Function name is: '{func.__name__}'")
        # виведем час виклику функції
        now = datetime.now()
        print(f"Today's date is: {now.strftime('%d.%m.%Y %H:%M')}")
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
print()
second_func(10)


# ==================== 11.2
# Створити кастомний Exception клас, який має повідомляти "Custom exception is occured"
class MyCustomException(Exception):
   print("\nCustom exception is occured\n")


# ==================== 11.3
# створюємо менеджер контексту
class MyCustomException_2:
    def __enter__(self):
        print('==========')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========\n')
        if exc_type:
            print(f'Exception: {exc_val}\n')
        return True

# вкладемо контекстний менеджер в try except
try:
    with MyCustomException_2():
        print("Program code execution")
except Exception as e:
    print(f'Exception: {e}')


# ==================== 11.4
# створимо конструкцію try except
try:
    print('=' * 10)
    print("Program code execution")
except Exception as e:
    print(f"Exception: {e}")
finally:
    print('=' * 10)
