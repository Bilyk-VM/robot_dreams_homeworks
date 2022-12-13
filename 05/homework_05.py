
# Перше завдання
while True:
    user_data = input("Введіть, будь ласка данні: ")
    if user_data == 'exit':                                 # створимо можливість вийти з програми
        print('Вихід з программи')
        break
    for char in user_data:                                  # перевіряємо кожен символ в послідовності данних
        if char.isdigit():                                  # перевірка на введення цифри
            char = int(char)                                # якщо цифра - переводим данні в int
            if char == 0:                                   # перевірим чи дорівнює число нулю
                print(f'Число {char}')
            elif char % 2 == 0:                             # перевірка на парність за допомогою ділення по модулю
                print(f"Число {char} - парне")
            else:
                print(f"Число {char} - не парне")
        elif char == ' ':                                   # якщо символ це пробіл - пропустимо ітерацію
            continue
        elif not char.isalnum():                            # перевіряємо чи введений символ взагалі буква чи цифра
            print(f"Введено символ - '{char}'")
        else:
            if char.istitle():                              # перевіряємо регістр літери за допомогою функції .istitle
                print(f"Велика літера - {char}")
            else:
                print(f"Маленька літера - {char}")
print()


# Друге завдання

import time                                                 # імпортуємо бібліотеку time
while True:
    print('I love Python')
    time.sleep(4.2)                                         # викличем функцію sleep

