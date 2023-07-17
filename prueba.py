import requests

def buscar_peliculas(query):
    url = f"https://api.themoviedb.org/3/search/movie?api_key=22b6427f0bbf7a0949366e0928a3253e&query={query}"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            resultados = data['results']
            for pelicula in resultados:
                print(pelicula['title'])
        else:
            print("Error al realizar la solicitud.")
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)


# Reemplaza 'TU_API_KEY' con tu propia clave de API de TMDb.
# Puedes obtener una clave de API gratuita registrándote en el sitio web de TMDb.
# Asegúrate de leer y cumplir con los términos y condiciones de TMDb al utilizar su API.
buscar_peliculas("pokemon")
