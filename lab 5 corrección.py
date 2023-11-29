#Axel Alberto Meza Mejias / C04845 Evelyn Feng Wu / B82870
#Lab 5
import abc
import argparse
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

# Definir la interfaz base
class ProcesadorBase(abc.ABC):
    @abc.abstractmethod
    def procesar_imagen(self):
        pass

# Implementar clases específicas para cada biblioteca
class ProcesadorPIL(ProcesadorBase):
    def __init__(self, imagen):
        self.imagen = imagen

    def procesar_imagen(self):
        img = Image.open(self.imagen)
        img.show()

class ProcesadorMatplotlib(ProcesadorBase):
    def __init__(self, imagen):
        self.imagen = imagen

    def procesar_imagen(self):
        img = mpimg.imread(self.imagen)
        plt.imshow(img)
        plt.axis('off')
        plt.show()

class ProcesadorOpenCV(ProcesadorBase):
    def __init__(self, imagen):
        self.imagen = imagen

    def procesar_imagen(self):
        img = cv2.imread(self.imagen)
        cv2.imshow('Imagen', img)
        key = cv2.waitKey(0)
        if key != -1:
            cv2.destroyAllWindows()

# Clase principal que maneja la selección de procesadores
class ProcesadorImagenes:
    def __init__(self, biblioteca, imagen):
        self.biblioteca = biblioteca
        self.imagen = imagen

    def procesar_imagen(self):
        procesador = self._seleccionar_procesador()
        procesador.procesar_imagen()

    def _seleccionar_procesador(self):
        if self.biblioteca == 'PIL':
            return ProcesadorPIL(self.imagen)
        elif self.biblioteca == 'Matplotlib':
            return ProcesadorMatplotlib(self.imagen)
        elif self.biblioteca == 'OpenCV':
            return ProcesadorOpenCV(self.imagen)
        else:
            raise ValueError("Biblioteca no válida. Seleccione PIL, Matplotlib o OpenCV.")

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de imágenes con PIL, Matplotlib y OpenCV")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True,
                        help="Especificar la biblioteca de procesamiento de imágenes a utilizar")
    parser.add_argument("--imagen", required=True, help="Especificar el nombre del archivo de imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()
    procesador = ProcesadorImagenes(args.biblioteca, args.imagen)
    procesador.procesar_imagen()

if __name__ == "__main__":
    main()