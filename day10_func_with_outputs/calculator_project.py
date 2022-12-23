def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide
}

def calculator():
    num1 = float(input("What's the first number? : "))
    for symbol in operations :
        print(symbol)  

    flag = True
    while flag :
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number? : "))
        cal_func = operations[operation_symbol]
        answer = cal_func(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Press 'y' to continue with {answer} or 'n' to exit : ") == 'y':
            num1 = answer
        else :
            flag = False
            calculator()

calculator()