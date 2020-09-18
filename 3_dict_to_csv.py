"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    with open('dict_to_csv.csv', 'w', encoding='utf-8') as file:
        list_of_dicts = [
            {'name': 'Иван','age': 23,'job': 'инженер'},
            {'name': 'Маша','age': 32,'job': 'маляр'},
            {'name': 'Ярополк','age': 93,'job': 'депутат'},
            {'name': 'Виктор','age': 65,'job': 'дизайнер'},
        ]
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter = ';')
        writer.writeheader()
        for dictionary in list_of_dicts:
            writer.writerow(dictionary)

if __name__ == "__main__":
    main()
