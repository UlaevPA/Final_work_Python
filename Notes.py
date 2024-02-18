def show_line(file_name:str):
    with open(file_name, 'r', encoding='utf-8') as f:
    number_note = input('Введите номер заметки: ')
    line = []
    for i, line in enumerate(f):
        if i in number_note:
            line.append(line.strip())

def show_all(file_name:str):
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))


def remove(file_name:str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        s = f'{last_name}, {first_name}, {patronymic}, {phone_number}\n'
        data.remove(s)
    with open(file_name, 'w',encoding='utf-8') as f:
        f.writelines(data)
        
        

def modify(file_name:str):
   
 
    old_data = find_by_attribute(file_name, True)
    
    print("Введите новые данные:\n")
    new_note = input('Новая заметка: ')
    body_note = input('Текст новой заметки: ')
    
    data = ""
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        data[i] = f'{new_note},\n {body_note}\n'
        
    with open(file_name, 'w',encoding='utf-8') as f:\
        f.writelines(data)



        
        
def find_by_name_note(file_name:str,option: bool):
    
        
    attr = input("Введите название заметки: ")
    with open(file_name, 'r',encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr,data))
        print(list(zip(range(1,len(data)+1),data)))
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя: ")
        return data[int(id)-1]
    


def add_new(file_name: str):
  
    new_note = input('Новая заметка: ')
    body_note = input('Текст заметки: ')

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{new_note}:\n {body_note}\n \n')

 
def main():
    file_name = 'notes.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все заметки')
        print('2 - добавить заметку')
        print('3 - удалить заметку')
        print('4 - изменить заметку')
        print('5 - поиск по названию заметки')
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
            print(find_by_name_note(file_name,False))
        elif answer == '6':
            show_line(file_name)
        elif answer == 'q':
            flag_exit = True

if __name__ == '__main__':
    main()
