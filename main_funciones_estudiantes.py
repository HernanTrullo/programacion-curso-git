import requests

def my_funcion_hernan_trullo():
    """
        Esta funcion es una funcion de prueba que accede a HTTP y hace un llamado a una API publica, vamos a 
        trabajar con CURL
    
    """
    url = "https://api.publicapis.org/entries"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Datos obtenidos de la API:")
        print(data)
    else:
        print(f"Error al acceder a la API. Código de estado: {response.status_code}")
        
        
def my_funcion_david(a, b):
    if b == 0:
        raise ZeroDivisionError("no se puede dividir por cero")
    return a / b

def main():
    while True:
        try:
            numero1 = float(input("Ingrese el primer numero: "))
            numero2 = float(input("Ingrese el segundo numero: "))

            resultado = my_funcion_david(numero1, numero2)
            print(f"El resultado de dividir {numero1} entre {numero2} es: {resultado}")
            break

        except ZeroDivisionError:
            print("Error: no se puede dividir por cero. Intente nuevamente.\n")
        except ValueError:
            print("Error: entrada invalida. Ingrese un numero valido.\n")


if __name__ == "__main__":
    main()
    


def my_funcion_daniel_ruales(a, b):
    return multiplicar(a, b)

def multiplicar(a, b):
    resultado = a * b
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
my_funcion_daniel_ruales()