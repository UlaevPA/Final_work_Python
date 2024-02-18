
def show_all(file_name:str):
   with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        for i, v in enumerate(data, 1):
            print(i,'.', v, '\n')
           


def remove(file_name:str):
    lines=[]
    with open(file_name, 'r', encoding='utf-8') as old:
        lines = old.readlines()
    with open(file_name, 'w', encoding='utf-8') as new:
        line_del = int(input("Введите номер строки для удаления: "))
        for number, line in enumerate(lines, 1):
            if number != line_del:
                new.write(line)
        

def modify(file_name:str):
   
 
    old_data = find_by_name_note(file_name, True)
    
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

        
        
def find_by_name_note(file_name: str, option: bool):
    
    with open(file_name, 'r',encoding='utf-8') as f:
        line = f.readlines()
        str_num = int(input("Введите строку заметки: "))
        for i, v in enumerate(line, 1):
            if i == str_num:
              return ("".join(v))
        
       

def add_new(file_name: str):
 
    new_note = input('Новая заметка: ')
    body_note = input('Текст заметки: ')

    with open(file_name, 'a', encoding='utf-8') as fd:
        fd.write(f'{new_note}: {body_note} \n')
        
        

 
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
        elif answer == 'q':
            flag_exit = True
        else:
            print('Введена неверная команда!')

if __name__ == '__main__':
    main()
