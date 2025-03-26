import os
import requests
import time

def descargar_imagenes(urls, directorio="imagenes_descargadas"):
    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    for i, url in enumerate(urls):
        try:
            respuesta = requests.get(url, stream=True)
            respuesta.raise_for_status()  # Verificar errores en la solicitud

            # Obtener la extensión del archivo desde la URL o usar .jpg por defecto
            extension = url.split('.')[-1]
            if len(extension) > 5:  # Si la extensión es muy larga, usar .jpg
                extension = "jpg"

            # Guardar la imagen en el directorio con un nombre numerado
            ruta_imagen = os.path.join(directorio, f"imagen_{i}.{extension}")
            with open(ruta_imagen, "wb") as archivo:
                for chunk in respuesta.iter_content(1024):
                    archivo.write(chunk)

            print(f"Imagen descargada: {ruta_imagen}")

        except requests.exceptions.RequestException as e:
            print(f"Error al descargar {url}: {e}")


"""urls_imagenes = [
    "https://i.pinimg.com/736x/16/cc/3e/16cc3e3da1bc4d8bca07b4d13b80b047.jpg"
    "https://kinsta.com/es/wp-content/uploads/sites/8/2021/02/what-is-a-url.jpeg"
    "https://www.shutterstock.com/image-vector/url-vector-icon-set-solid-260nw-2495168965.jpg"
    "https://www.shutterstock.com/image-vector/internet-connection-global-digital-communication-260nw-2237737371.jpg"
    "https://i.pinimg.com/736x/21/ec/ba/21ecbaa88f7846052baa9a4ebbf9444d.jpg"
    "https://i.pinimg.com/736x/1c/05/e8/1c05e8d9520951cae53ff245f5c360ae.jpg"
    "https://i.pinimg.com/736x/aa/35/c8/aa35c84fce8a80c30bb4199f7ae06e5a.jpg"
    "https://i.pinimg.com/736x/77/70/53/777053222e4fb29f4c8c5046bfbc86fc.jpg"
    "https://i.pinimg.com/736x/ac/20/03/ac2003c882553cfcc1832c4d975d805a.jpg"
    "https://i.pinimg.com/736x/41/06/b3/4106b37e6f8483a756ab76fc1531af16.jpg"
    "https://i.pinimg.com/736x/60/af/1b/60af1b178b207dc1f52d02a57c6354b0.jpg"
    "https://i.pinimg.com/736x/00/fd/87/00fd8720aa18ef96acb1517274736ee3.jpg"
    "https://i.pinimg.com/736x/92/ed/56/92ed56765faed01856ffae8b728f887b.jpg"
    "https://i.pinimg.com/736x/9e/8f/60/9e8f606af9385d4de57b946e65d9b76d.jpg"
    "https://i.pinimg.com/736x/de/6b/63/de6b63d82b141c37ab57152b44a73fae.jpg"

]"""

urls_imagenes = [
    "https://images.pexels.com/photos/34950/pexels-photo.jpg",
    "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
    "https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg",
    "https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg",
    "https://images.pexels.com/photos/1308889/pexels-photo-1308889.jpeg",
    "https://images.pexels.com/photos/459225/pexels-photo-459225.jpeg",
    "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg",
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
    descargar_imagenes(urls_imagenes)
    tf = time.time()
    print(f"Tiempo total: {tf-ti}")
