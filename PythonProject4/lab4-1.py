import math
import datetime

def square(num):
    result=math.sqrt(num)
    print(f"Корень числа {num} - {result}")

try:
    a=float(input("Введите число: "))
except ValueError:
    print("Недопустимое значение")

square(a)


print("Текущее время: ", datetime.datetime.now())