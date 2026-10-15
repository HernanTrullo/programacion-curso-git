print("Hello Wolrd - From GIT HUB")


def operation_suma(a, b):
    return a + b

def operation_resta(a, b):
    return a - b

def operations_multiplicacion(a, b):
    return a * b

def operations_division(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    
    return a / b

def new_function():
    pass




def sumar(a, b):
    return a + b

n1 = int(input("Dame el primer número: "))
n2 = int(input("Dame el segundo: "))

print(f"La suma es: {sumar(n1, n2)}")
#funcion de Guillermo