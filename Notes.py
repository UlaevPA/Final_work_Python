import csv
import datetime
import pandas as pd

def show_all(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            print("ID заметки", "Название заметки",
                  "Текст заметки", "Дата заметки")
            print(row["ID заметки"], row["Название заметки"],
                  row["Текст заметки"], row["Дата заметки"])


def remove(file_name: str):
    df = pd.read_csv(file_name)
    print(df)
    del_line = int(input('Введите индекс строки для удаления: '))
    df = df.drop(del_line)
    df.to_csv(file_name, index=False)
            

    


def modify(file_name: str):
    df = pd.read_csv(file_name)
    print(df)

    mod_line = input('Введите ID заметки: ')
    fields_to_change = input('Какие данные Вы хотите изменить? ').split(',')
    data_to_update = {}
    for field in fields_to_change:
        data_to_update[field] = input(f'Введите {field}: ')

    df = pd.read_csv(file_name).set_index('ID заметки')
    df.loc[mod_line, fields_to_change] = data_to_update
    df.to_csv(file_name)
    print('Спасибо, данные обновлены')
    


def find_by_name_note(file_name: str, option: bool):

    with open(file_name, 'r', encoding='utf-8') as f:
        line = f.readlines()
        str_num = int(input("Введите строку заметки, кроме первой: "))
        for i, v in enumerate(line, 1):
            if i == 1:
                print("Первая строка является шапкой заметки")
            elif i == str_num:
                return ("".join(v))


def fields(file_name: str):
    field = ["ID заметки", "Название заметки", "Текст заметки", "Дата заметки"]
    with open(file_name, '+r', encoding='utf-8', newline='') as f:
        data = csv.writer(f, delimiter=';', lineterminator='\n')
        data.writerow(field)


def add_new(file_name: str):
    from csv import writer
    id_num = int(input('Введите ID заметки: '))
    new_note = input('Новая заметка: ')
    body_note = input('Текст заметки: ')
    date_create = datetime.date.today()
    all_name = [id_num, new_note.title(), body_note.title(), date_create]
    with open(file_name, 'a+', encoding='utf-8', newline='') as f:
        data = writer(f, delimiter=';', lineterminator="\r")
        data.writerow(all_name)
        fields(file_name)


def main():
    file_name = 'notes.csv'
    flag_exit = False

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
            add_new(file_name)
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
