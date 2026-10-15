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


#funcion de thomas caclular promedio
def my_funcion_thomas():
    nombre = input("Ingrese su nombre: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 3.0:
        print(f"{nombre}, su promedio es {promedio:.2f}. ¡Felicidades, ha aprobado!")
    else:
        print(f"{nombre}, su promedio es {promedio:.2f}. Lo siento, ha reprobado.")
    
    print("fin de la funcion")
    
        
def segunda_funcion_de_hernan():
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
