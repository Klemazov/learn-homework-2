"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as file:
        origin_referat = file.read()
        print(f'В исходном тексте {len(origin_referat)} символов')
        number_of_words = len(origin_referat.split())
        print(f'Число слов в исходном тексте: {number_of_words}')
        referat_with_exlamation_marks = origin_referat.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as new_referat:
        new_referat.write(referat_with_exlamation_marks)

if __name__ == "__main__":
    main()
