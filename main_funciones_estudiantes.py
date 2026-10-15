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


#funcion thomas-calcular notas
def my_funcion_thomas():
    print("Ingrese las notas de los estudiantes:")
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    promedio = (nota1 + nota2 + nota3) / 3
    print(f"El promedio de {nombre} es: {promedio}")
    if promedio >= 3.0:
        print(f"{nombre} ha aprobado.")
    else:
        print(f"{nombre} ha reprobado.")
        


