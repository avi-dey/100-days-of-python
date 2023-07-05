num1 = int(input("enter number 1 "))
num2 = int(input("enter number 2 "))

guess1 = int(input("enter guess 1 "))
guess2 = int(input("enter guess 2 "))

def guess_checker(num1, num2, guess1, guess2):
    if num1 > num2:
        return num1 == guess1
    else:
        return num2 == guess2

print(guess_checker(num1, num2, guess1, guess2))
