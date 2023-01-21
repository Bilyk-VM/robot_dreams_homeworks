import json

my_dict = {
    'Dima': 1234,
    'Maks': 2234,
    'Stas': 3234,
    'Tim': 4234,
    'Oleksiy': 5234
}

# Перевіримо чи існує файл phonebook.txt, якщо ні, то створимо його із заздалегідь створеною базою абонентів (my_dict)
try:
    with open('phonebook.txt') as book:
        json.load(book)
except:
    with open('phonebook.txt', 'w') as book:
        json.dump(my_dict, book, indent=2, ensure_ascii=False) # indent дозволяє впорядковувати данні більш наочно


# створюємо вічний цикл, щоб запроси йшли постійно, але зробимо можливість вийти, за допомогою вводу команди "exit"
while True:
    user_input = input("Введіть команду, ім'я та номер телефону: ")
    if user_input == 'exit':
        print('Вихід\n')
        break

# перевірка на ввід команди "stats" з підрахунком кількості абонентів в телефонній книзі
    elif user_input == 'stats':
        with open('phonebook.txt') as book:
            my_dict = json.load(book)
            print(f"\nКількість абонентів в телефонній книзі: {len(my_dict)}\n")
        continue

# превірка на ввід команди "list" з виводом усіх імен абонентів в телефонній книзі. Вивід на кожній стрічці окремо
    elif user_input == 'list':
        with open('phonebook.txt') as book:
            my_dict = json.load(book)
            print(f"\nСписок всіх імен в телефонній книзі: ")
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
        print('Невірний формат вводу, спробуйте ще раз\n')
        continue

# перевіряємо на введення команди "add", якщо абонент вже є - повідомимо про це, якщо ні - добавимо в книгу
    if comand == 'add':
        with open('phonebook.txt', 'r+') as book:
            my_dict = json.load(book)
            if my_dict.get(name) is None:
                my_dict[name] = tel
                print(my_dict)
                with open('phonebook.txt', 'w') as book:
                    json.dump(my_dict, book, indent=2, ensure_ascii=False)
                print(f'Створюєм новий запис абонента {name} з номером {tel}\n')
            else:
                print(f'Абонент {name} вже присутній у телефонній книзі\n')

# перевірка на введення команди "delete" для видалення абонента з книги
    if comand == 'delete':
        with open('phonebook.txt', 'r+') as book:
            my_dict = json.load(book)
            if my_dict.get(name) is None:
                print(f"Абонента {name} з номером {tel} немає в телефонній книзі\n")
            else:
                del my_dict[name]
                with open('phonebook.txt', 'w') as book:
                    json.dump(my_dict, book, indent=2, ensure_ascii=False)
                print(f"Видаляємо абонента {name} з телефонної книги\n")

# перевірка на введення команди "show", з виводом детальної інформації про абонента
    if comand == 'show':
        with open('phonebook.txt', 'r+') as book:
            my_dict = json.load(book)
            if my_dict.get(name) is None:
                print(f"Абонента {name} немає в телефонній книзі\n")
            else:
                print(f'Абоненту {name}, відповідає номер телефону: {my_dict.get(name)}\n')




