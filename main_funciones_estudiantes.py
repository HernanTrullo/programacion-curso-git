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


def my_funcion_daniel_ruales(a, b):
    return multiplicar(a, b)

def multiplicar(a, b):
    resultado = a * b
    return resultado

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
my_funcion_daniel_ruales()