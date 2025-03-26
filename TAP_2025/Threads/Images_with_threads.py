import os
import requests
import time
import concurrent.futures

# Función para descargar una sola imagen
def descargar_imagen(url, index, directorio="imagenes_descargadas_hilos"):
    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    try:
        respuesta = requests.get(url, stream=True, timeout=10)
        respuesta.raise_for_status()  # Verificar errores en la solicitud

        # Obtener la extensión desde la URL o usar ".jpg" por defecto
        extension = url.split('.')[-1].split("?")[0]  # Elimina parámetros en la URL
        if len(extension) > 5:  # Si la extensión es sospechosamente larga, usar ".jpg"
            extension = "jpg"

        # Guardar la imagen en el directorio con un nombre numerado
        ruta_imagen = os.path.join(directorio, f"imagen_{index}.{extension}")
        with open(ruta_imagen, "wb") as archivo:
            for chunk in respuesta.iter_content(1024):
                archivo.write(chunk)

        print(f"Imagen descargada: {ruta_imagen}")

    except requests.exceptions.RequestException as e:
        print(f"Error al descargar {url}: {e}")

# Lista de URLs de imágenes
urls_imagenes = [
    "https://images.pexels.com/photos/34950/pexels-photo.jpg",
    "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
    "https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg",
    "https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg",
    "https://images.pexels.com/photos/1308889/pexels-photo-1308889.jpeg",
    "https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg",
    "https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg",
    "https://images.pexels.com/photos/1558729/pexels-photo-1558729.jpeg",
    "https://images.pexels.com/photos/301920/pexels-photo-301920.jpeg",
    "https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg",
    "https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg",
    "https://images.pexels.com/photos/356056/pexels-photo-356056.jpeg",
    "https://images.pexels.com/photos/1402787/pexels-photo-1402787.jpeg",
    "https://images.pexels.com/photos/267885/pexels-photo-267885.jpeg"
]

if __name__ == "__main__":
    ti = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(descargar_imagen, urls_imagenes, range(len(urls_imagenes)))
    tf = time.time()
    print(f"Tiempo total: {tf - ti} segundos")



