'''
# Task one ======================================
phrase = 'I love Python'
kilkist = input('Введіть кількість повторень: ')
print(('' + phrase + '') * int(kilkist))
print()

# Task two ======================================
age_in_month = input('Введіть свій вік в місяцях: ')
age_in_month = int(age_in_month)
print('Ваш вік -',  age_in_month, 'місяців ')

# Task three ======================================
age_in_years = age_in_month // 12
print('Тобто на даний момент вам -', age_in_years, 'років ')
print()

# Task four ======================================
my_name = input('Введіть будьласка своє імя: ')
my_age = 'My name is ' + my_name + '. I`m ' + str(age_in_years) + ' years old.'
print(my_age)
print()
'''
# Task five ======================================
zminna_1 = input('Введіть значення першої змінної: ')
zminna_1 = int(zminna_1)
for i in range(1, 6):
    print('Значення першої змінної дорівнює', zminna_1)
    zminna_2 = input('Введіть значення другої змінної: ')
    print('Значення оператора ==', zminna_1 == int(zminna_2))
    print('Значення оператора !=', zminna_1 != int(zminna_2))
    print('Значення оператора >=', zminna_1 >= int(zminna_2))
    print('Значення оператора >', zminna_1 > int(zminna_2))
    print('Значення оператора <=', zminna_1 <= int(zminna_2))
    print('Значення оператора <', zminna_1 < int(zminna_2))
    print()
    i += i
print()
'''
# Task six ======================================
a = 2
print('Змінна а =', a)
b = 5
print('Змінна b =', b)
c = 6
print('Змінна c =', c)
d = str(a) + str(b) + str(c)
print('По умовам задачі, змінна d дорівнює:', d)
'''