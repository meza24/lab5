# Autor: Axel Alberto Meza Mejias / C04845
# Autor: Evelyn Feng Wu / B82870
# Descripcion: Programa que abre y muestra una imagen usando PIL, Matplotlib o OpenCV
# Fecha: 18/11/2023

# Importar el módulo argparse para procesar los argumentos de la línea de comandos
import argparse

'''
Función para procesar los argumentos de la línea de comandos usando el módulo argparse y devolver un objeto con los argumentos 
procesados. El objeto devuelto contiene los valores de los argumentos de la línea de comandos.
'''
def parse_args():
    # Crear un objeto ArgumentParser para procesar los argumentos de la línea de comandos 
    parser = argparse.ArgumentParser(description="Procesamiento de imágenes con PIL, Matplotlib y OpenCV")
    # Agregar los argumentos de la línea de comandos que se van a procesar 
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True,
                        # Agregar una descripción para el argumento --biblioteca que se va a procesar 
                        help="Especificar la biblioteca de procesamiento de imágenes a utilizar")
    # Agregar el argumento de la línea de comandos --imagen para especificar el nombre del archivo de imagen a procesar
    parser.add_argument("--imagen", required=True, help="Especificar el nombre del archivo de imagen a procesar")
    # Devolver el objeto con los argumentos procesados 
    return parser.parse_args()

# Función principal 
def main():
    # Procesar los argumentos de la línea de comandos y devolver un objeto con los argumentos procesados
    args = parse_args()
    
    # Mostrar el valor de los argumentos procesados 
    if args.biblioteca == 'PIL':
        # Lógica para abrir y mostrar la imagen usando PIL (Python Imaging Library)
        from PIL import Image

        #Manejo de excepciones para el manejo de errores en la apertura de la imagen 
        try:

            #Abrir la imagen y mostrarla
            img = Image.open(args.imagen)
            img.show()
        
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con PIL: {e}")
    
    # Mostrar el valor de los argumentos procesados 
    elif args.biblioteca == 'Matplotlib':
        # Lógica para abrir y mostrar la imagen usando Matplotlib 
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        
        try:
            img = mpimg.imread(args.imagen)
            plt.imshow(img) # Mostrar la imagen usando Matplotlib
            plt.axis('off')  # Desactivar los ejes
            plt.show() # Mostrar la imagen usando Matplotlib
        
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con Matplotlib: {e}")

    elif args.biblioteca == 'OpenCV': 
        # Lógica para abrir y mostrar la imagen usando OpenCV
        import cv2 # Importar el módulo OpenCV para procesamiento de imágenes
        
        try:
            img = cv2.imread(args.imagen) # Leer la imagen usando OpenCV
            cv2.imshow('Imagen', img)  # Mostrar la imagen usando OpenCV
            cv2.waitKey(0) # Esperar a que el usuario presione cualquier tecla
            cv2.destroyAllWindows() # Cerrar todas las ventanas abiertas por OpenCV
        
        # Manejo de excepciones para el manejo de errores en la apertura de la imagen
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con OpenCV: {e}")

    else:
        print("Biblioteca no válida. Seleccione PIL, Matplotlib o OpenCV.")

# Llamar a la función principal 
if __name__ == "__main__":
    main()
