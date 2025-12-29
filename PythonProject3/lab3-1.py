def file_read(file):
    with open(file, 'r') as file:
        content = file.read()
        print(content)

def file_sread(file):
    with open(file, 'r') as file:
        counter=1
        for line in file:
            print(f"{counter}.", line)
            counter+=1

c=int(input("Режим чтения(полное - 1, построчное - 2): "))
if c==1:
    file_read('example.txt')
elif c==2:
    file_sread('example.txt')
else:
    print("недопустимый результат")