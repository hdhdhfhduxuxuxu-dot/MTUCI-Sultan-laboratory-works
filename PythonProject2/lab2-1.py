#Задание 1
def greet(name):
    return name

person=str(input("Как вас зовут?: "))
result1=greet(person)
print("Привет, ", result1)

#Задание 2

def square(number):
    number=number**2
    return number

n=int(input("Введите число: "))
result2=square(n)
print("Квадрат вашего числа: ", result2)

#Задание 3

def max_of_two(x, y):
    if x!=y:
        if x>y:
            return x
        else:
            return y
    else:
        print("Числа одинаковые")

numb1=int(input("Введите первое число: "))
numb2=int(input("Введите второе число: "))
result3=max_of_two(numb1, numb2)
print("Наибольшее число: ", result3)