Laboratorio #5

Descripción
Este software desarrollado en Python tiene como propósito abrir y mostrar imágenes, empleando bibliotecas Matplotlib, PIL y OpenCV. El enfoque principal se dirige hacia la modularidad del diseño del programa, aprovechando clases y propiedades para garantizar una estructura bien definida y ordenada.

Diagrama de Diseño:
https://github.com/meza24/lab5/blob/main/Diagrama3.png?raw=true

Dependencias del Proyecto.

PIL (Python Imaging Library)
La biblioteca PIL se emplea para procesamiento y manipulación básica de imágenes en Python. La dependencia clave es:
from PIL import Image (parte de la biblioteca estándar de Python)

Matplotlib:

Matplotlib se utiliza para la visualización de datos y, en este caso, para mostrar imágenes.
Dependencias:
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
Matplotlib es una biblioteca externa, y su instalación se realiza a través de pip install matplotlib.

OpenCV:

OpenCV es una biblioteca muy utilizada para el procesamiento de imágenes en tiempo real.
Dependencias:
import cv2
OpenCV es una biblioteca externa y se instala mediante pip install opencv-python.


Instalación

Pasos:
1. Clona el repositorio:
    git clone https://github.com/meza24/lab5.git

2. Instala las dependencias:
    pip install pillow matplotlib opencv-python-headless

Uso del Programa:

Pasos:
1. Comando para correr el programa:

   - General:
    python3 ruta_completa_hacia_el_script/lab5.py --biblioteca PIL --imagen ruta_completa_hacia_la_imagen/imagen.png

   - Desde el mismo directorio donde se encuentran el script y la imagen:
    python3 lab5.py --biblioteca PIL --imagen imagen.png

   - Ejemplo:
    python3 ~/Escritorio/progra/python/lab5/lab5.py --biblioteca PIL --imagen imagen.png

Consideraciones Importantes:
- La instalación previa de las bibliotecas Matplotlib y OpenCV es esencial para la ejecución exitosa del programa.
- Asegúrate de que las versiones de las bibliotecas sean compatibles para evitar posibles problemas o errores en la ejecución del código.

Autor
Axel Alberto Meza Mejias / C04845
