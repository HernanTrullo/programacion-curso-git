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
    
def my_funcion_Andres_Guauña():
    
   def operar():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)

    except ValueError:
        print("Error: debes ingresar números válidos.")


