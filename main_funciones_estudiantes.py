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


def my_funcion_daniel_ruales():
    def sumar_matrices(A, B):
    C = []
    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)
    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(sumar_matrices(A, B))