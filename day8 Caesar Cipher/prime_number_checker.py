from math import floor
def is_prime(number):
    # number is only divible by itself and 1
    # we only need to in the range of [2,num/2]
    # after num/2 it's just mirror factors
    for i in range(2, floor(number/2) +1):
        if number % i == 0:
            return False
    return True


num = int(input("enter the number: "))
ans = is_prime(num)
print(f"{num} is prime: {ans}")