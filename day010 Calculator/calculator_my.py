def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

caculator_on = True
continue_calc_with_n1 = True

while caculator_on:
    continue_calc_with_n1 = True
    n1 = int(input("What's the first number?: "))
    # loop
    while continue_calc_with_n1:
        option = input("Choose any of the following options: \n+ \n- \n* \n/ \n")
        
        while option != "+" and option != "-" and option != "*" and option != "/":
            option = input("Invalid input. Please choose one of: \n+ \n- \n* \n/ \n")
        n2 = int(input("What's the second number?: "))
        
        if option == "+":
            res = add(n1,n2)
        elif option == "-":
            res = subtract(n1,n2)
        elif option == "*":
            res = multiply(n1,n2)
        else:
            res = divide(n1,n2)
        print(f"OUTPUT : {n1} {option} {n2} = {res}")
        
        next_calc = input(f"Type 'y' to continue calculating with first number : '{n1}', or type 'n'(new) to start a new calculation, or type 'q' to quit").lower()
        while next_calc != "y" and next_calc != "n" and next_calc != "q":
            next_calc = input(f"INVALID INPUT!! Type 'y' to continue calculating with first number : '{n1}', or type 'n'(new) to start a new calculation, or type 'q' to quit").lower()
        
        if next_calc == "n":
            continue_calc_with_n1 = False
        elif next_calc == "y":
            break
        else:
            caculator_on = False
            break