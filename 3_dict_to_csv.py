"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    list_of_dict = [
        {'name': 'Саша', 'age': 19, 'job': 'Грузчик'},
        {'name': 'Петя', 'age': 23, 'job': 'Главный грузчик'}, 
        {'name': 'Коля', 'age': 30, 'job': 'Грузчик'}, 
        {'name': 'Вася', 'age': 33, 'job': 'Грузчик'}        
    ]

    with open("list_of_dict.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "job"])
        writer.writeheader()
        writer.writerows(list_of_dict)

    print("Файл people.csv сохранён")


if __name__ == "__main__":
    main()
