# return vs print
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

# dict with function names
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

n1 = float(input("What's the first number?: "))
for key in operators:
    print(key)
operation = input("Choose operation: \n")
n2 = float(input("What's the second number?: "))
# if operation == "+":
#     result = add(n1,n2)
# elif operation == "-":
#     result = subtract(n1,n2)
# elif operation == "*":
#     result = multiply(n1,n2)
# else:
#     result = divide(n1,n2)
calc_func = operators[operation] # calc_func will become the name of the function
result = calc_func(n1, n2)
print(f"OUTPUT : {n1} {operation} {n2} = {result}")
n1 = result