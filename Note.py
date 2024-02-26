import csv
import datetime
import pandas as pd


def show_all(file_name):
    df = pd.read_csv(file_name)
    print(df)


def remove(file_name: str):
    df = pd.read_csv(file_name)
    print(df)
    del_line = int(input('Введите индекс строки для удаления: '))
    df = df.drop(del_line)
    df.to_csv(file_name, header=True, index=False)


def modify(file_name: str):
    df = pd.read_csv(file_name, header=None)
    print(df)

    mod_line = input('Введите ID заметки: ')
    fields_to_change = input('Введите "1" если хотите изменить "Название заметки" или "2" если "Текст заметки": ')
    if fields_to_change == '1':
        df.loc[mod_line, 'Название заметки'] = input('Введите новое название: ')
        df.to_csv(file_name, index=False, header=None)
    elif fields_to_change == '2':
        df.loc[mod_line, 'Текст заметки'] = input('Введите новый текст: ')
        df.to_csv(file_name, index=False, header=None)
    else:
        print('Неправильный выбор')


def find_by_name_note(file_name: str, option: bool):
    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readlines()
        str_num = int(input("Введите строку заметки, кроме первой: "))
        for i, v in enumerate(line, 1):
            if i == 1:
                print("Первая строка является шапкой заметки")
            elif i == str_num:
                return ("".join(v))


def write_to_csv(data):
    with open('notes.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE)
        writer.writerow(data)


def main():
    file_name = 'notes.csv'
    flag_exit = False
    headers = ['ID заметки', 'Название заметки', 'Текст заметки', 'Дата заметки']
    write_to_csv(headers)

    while not flag_exit:
        print('1 - показать все заметки')
        print('2 - добавить заметку')
        print('3 - удалить заметку')
        print('4 - изменить заметку')
        print('5 - поиск по номеру заметки')
        answer = input('Введите операцию или q для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            id_note = input("Введите ID заметки: ")
            title = input("Введите название заметки: ")
            text = input("Введите текст заметки: ")
            date = datetime.date.today()
            data = [id_note, title.title(), text.title(), date]
            write_to_csv(data)
        elif answer == '3':
            remove(file_name)
        elif answer == '4':
            modify(file_name=file_name)
        elif answer == '5':
            print(find_by_name_note(file_name, False))
        elif answer == 'q':
            flag_exit = True
        else:
            print('Введена неверная команда!')


if __name__ == '__main__':
    main()
