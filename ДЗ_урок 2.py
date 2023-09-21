# Задание 1

# HELP = """
# help - напечатать справку по программе.
# add - добавить задачу в список (название задачи запрашиваем у пользователя).
# show - напечатать все добавленные задачи."""
#
# tasks = []
#
# run = True
#
# while run:
#     command = input("Введите команду: ")
#     if command == "help":
#         print(HELP)
#     elif command == "show":
#         print(tasks)
#     elif command == "add":
#         task = input("Введите название задачи: ")
#         tasks.append(task)
#         print("Задача добавлена")
#     elif command == "exit":
#         print("Спасибо за использование! До свидания!")
#         break
#     else:
#         print("Неизвестная команда")
#         break
#
# print("До свидания!")

# Задание 2
HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

tasks = []
today = []
tomorrow = []
other = []
run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена")
        data = input("Введите дату выполнения задачи, (Сегодня, Завтра, Позже)  :   ")
        if data == "Сегодня":
            today.append(task)
            print("Задача добавлена в список Сегодня")
        elif data == "Завтра":
            tomorrow.append(task)
            print("Задача добавлена в список Завтра")
        elif data == "Позже":
            other.append(task)
            print("Задача добавлена в список Позже")
        else:
            print("Неизвестная команда")
    elif command == "exit":
        print("Спасибо за использование! До свидания!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")