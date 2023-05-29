# divisble by 3 fizz
# by 5 buzz
# by both 3 and 5 fizzbuzz
# do from 0 to 100

# catch is: you have to put 15 up top.
# if you put divisibility by 3 or 5 up top
# then fizzbuzz will never get printed
for num in range(101):
    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print("fizz")
    else: print(num)