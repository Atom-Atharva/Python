a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Insert Simple Arithmetic Operator: ")

if (op == '+'):
    print(a+b)

elif (op == '-'):
    print(a-b)

elif (op == '*'):
    print(a*b)

elif (op == '/'):
    print(a/b)

elif (op == '%'):
    print(a % b)

else:
    print("Invalid Choice :( ")
