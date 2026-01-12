def is_prime(number):
    if number<=1 or number%2==0 or number%3==0 or number%5==0 or number%7==0:
        return False
    else:
        return True

our_num=int(input("Введите число: "))
r=is_prime(our_num)
print(r)
