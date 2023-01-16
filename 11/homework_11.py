# ==================== 11.1
# Написати декоратор
# імпортуємо datetime
from datetime import datetime

# створимо декоратор, який буде доповнювати функції їх назвою та часом виклику
def deco(func):
    def inner(*args, **kwargs):
        # виведем назву функції, за допомогою методу __name__
        print(f"\nFunction name is: '{func.__name__}'")
        # виведем час виклику функції
        now = datetime.now()
        print(f"Today's date is: {now.strftime('%d.%m.%Y %H:%M')}")
        # викликаємо функцію, яка буде декоруватись
        func(*args, **kwargs)
    return inner

# задекоруємо декілька простих функцій
@deco
def first_func():
    print('This is the first function')

@deco
def second_func():
    print('This is the second function')

# викличем ці функції
first_func()
print()
second_func()


# ==================== 11.2
# Створити кастомний Exception клас, який має повідомляти "Custom exception is occured"
class MyCustomException(Exception):
   print("Custom exception is occured")


# ==================== 11.3
# створюємо менеджер контексту
class MyCustomException_2:
    def __enter__(self):
        print('==========')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('==========')

# вкладемо контекстний менеджер в try except
try:
    with MyCustomException_2():
        print("\nProgram code execution\n")
except Exception as e:
    print(f'Exception: {e}')


# ==================== 11.4
# створимо конструкцію try except
try:
    print('=' * 10)
    print("\nProgram code execution\n")
except Exception as e:
    print('=' * 10)
    print(f"Exception: {e}")