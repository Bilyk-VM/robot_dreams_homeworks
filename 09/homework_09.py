# Створити програму, яка буде приймати число і друкувати відповідне число в послідовності Фібоначчі
# =============================== Напишем программу за допомогою генератора:
def fibo(n):
    a = b = 1                           # першим двум елементам присвоюємо значення 1
    for i in range(2, n):
        a, b = b, a + b                 # розрахунок елемента послідовності Фібоначчі
    yield b                             # змінна b - потрібне нам число

n = int(input("Введіть порядковий номер елемента, який більше нуля: "))

if n > 0:                               # перевіримо чи введений номер більше нуля
    res = fibo(n)
                                        # викличем функцію next з результатом нашого генератора - надрукуємо результат
    print(f"Число Фібоначчі з таким порядковим номером дорівнює: {next(res)}")
else:
    print("Порядковий номер не задовольняє умову")


# =============================== Напишем программу за допомогою ітератора:
class Fibo:
    def __init__(self):
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self
                                                    # розрахунок числа ФІбоначчі
    def __next__(self):
        self.c = self.a
        self.a = self.b
        self.b = self.c + self.a
        return self.c

n = int(input("Введіть число більше нуля: "))
                                                     # перевіримо чи введений номер більше нуля
if n > 0:
    f = Fibo()
    i = iter(f)
    for x in range(n):                               # за допомогою цикла for виведемо послідовність ряду
        print(next(i), end = ' ')
else:
    print("Порядковий номер не задовольняє умову")



# ================================ Напишем программу за допомогою рекурсії:
def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)

n = int(input("Введіть порядковий номер елемента, який більше нуля: "))

if n > 0:                                               # перевіримо чи введений порядковий номер більше нуля
    print(f"Число Фібоначчі з таким порядковим номером дорівнює: {fibo(n)}")
else:
    print("Порядковий номер не задовольняє умову")
# P.S. Цей спосіб є дуже не ефективним для підрахунку таких задач



# Написати програму, яка буде повертати факторіал введеного числа, використовуючи рекурсію
def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x

x = int(input("Введіть число, більше нуля: "))
if x > 0:
    print(f"Факторіал числа {x}, дорівнює {fact(x)}")
else:
    print(f"Число {x}, не задовільняє умову")