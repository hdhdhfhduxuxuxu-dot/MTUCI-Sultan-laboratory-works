def add_text(filename, txt):
    with open(filename, "a") as f:
        f.write("\n"+f"{txt}")
    return "Текст успешно добавлен"

def new_text(filename, txt):
    with open(filename, 'w') as f:
        f.write(txt)
    return "Текст успешно создан"

try:
    c=1
    while c==1 or c==2:
        c=int(input("Продолжить писать - 1, создать новый файл - 2, закончить писать - любое другое значение: "))
        if c==1:
            txt=input("Введите добавочный текст: ")
            result=add_text(filename, txt)
            print(result)
        elif c==2:
            txt = input("Введите содержимое нового файла: ")
            filename=input("Введите имя файла: ")
            result=new_text(filename, txt)
            print(result)
        else:
            print("Конец записи")
except ValueError:
    print("Конец записи")