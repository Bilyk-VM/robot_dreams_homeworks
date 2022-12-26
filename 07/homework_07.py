
# створимо словник
my_dict = {
    'Dima': 1234,
    'Maks': 2234,
    'Stas': 3234,
    'Tim': 4234,
}

# створюємо вічний цикл, щоб запроси йшли постійно, але зробимо можливість вийти, за допомогою вводу команди "exit"
while True:
    user_input = input("Введіть команду, ім'я та номер телефону: ")
    if user_input == 'exit':
        print('Вихід\n')
        break

# перевірка на ввід команди "stats" з підрахунком кількості абонентів в телефонній книзі
    elif user_input == 'stats':
        print(f"Кількість абонентів в телефонній книзі: {len(my_dict)}\n")
        continue

# превірка на ввід команди "list" з виводом усіх імен абонентів в телефонній книзі. Вивід на кожній стрічці окремо
    elif user_input == 'list':
        print(f"Список всіх імен в телефонній книзі: ")
        for k in my_dict.keys():
            print(k)
        print()
        continue

# розділимо введені данні на змінні з перевіркою введення на кількість слів
    split_input = user_input.split()
    if len(user_input.split()) == 3:
        comand = split_input[0]
        name = split_input[1]
        tel = int(split_input[2])
    elif len(user_input.split()) == 2:
        comand = split_input[0]
        name = split_input[1]
        tel = 'unkonwn'
    else:
        print('Невірний формат вводу, спробуйте ще раз')
        continue

# перевіряємо на введення команди "add", якщо абонент вже є - повідомимо про це, якщо ні - добавимо в книгу
    if comand == 'add':
        if my_dict.get(name) is None:
            my_dict[name] = tel
            print(f'Створюєм новий запис абонента {name} з номером {tel}\n')
        else:
            print(f'Абонент {name} вже присутній у телефонній книзі\n')

# перевірка на введення команди "delete" для видалення абонента з книги
    if comand == 'delete':
        if my_dict.get(name) is None:
            print(f"Абонента {name} з номером {tel} немає в телефонній книзі\n")
        else:
            del my_dict[name]
            print(f"Видаляємо абонента {name} з телефонної книги\n")

# перевірка на введення команди "show", з виводом детальної інформації про абонента
    if comand == 'show':
        if my_dict.get(name) is None:
            print(f"Абонента {name} немає в телефонній книзі\n")
        else:
            print(f'Абоненту {name}, відповідає номер телефону: {my_dict.get(name)}\n')
