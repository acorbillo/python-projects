
def calculator():
    try:
        x = float(input("enter a number: "))
        op = str(input("operation (+, -, *, /): "))
        y = float(input("enter a number: "))
    
        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else: 
            return ("invalid input")

    except ValueError:
        print("invalid")

print("answer:", calculator())
