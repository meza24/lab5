import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Procesamiento de imágenes con PIL, Matplotlib y OpenCV")
    parser.add_argument("--biblioteca", choices=["PIL", "Matplotlib", "OpenCV"], required=True,
                        help="Especificar la biblioteca de procesamiento de imágenes a utilizar")
    parser.add_argument("--imagen", required=True, help="Especificar el nombre del archivo de imagen a procesar")
    return parser.parse_args()

def main():
    args = parse_args()
    
    if args.biblioteca == 'PIL':
        # Lógica para abrir y mostrar la imagen usando PIL (Python Imaging Library)
        from PIL import Image

        try:
            img = Image.open(args.imagen)
            img.show()
        
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con PIL: {e}")
    
    elif args.biblioteca == 'Matplotlib':
        # Lógica para abrir y mostrar la imagen usando Matplotlib 
        import matplotlib.pyplot as plt
        import matplotlib.image as mpimg
        
        try:
            img = mpimg.imread(args.imagen)
            plt.imshow(img)
            plt.axis('off')  
            plt.show()
        
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con Matplotlib: {e}")

    elif args.biblioteca == 'OpenCV':
        # Lógica para abrir y mostrar la imagen usando OpenCV
        import cv2
        
        try:
            img = cv2.imread(args.imagen)
            cv2.imshow('Imagen', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
        except FileNotFoundError:
            print("Error: Archivo de imagen no encontrado.")
        
        except Exception as e:
            print(f"Error al procesar la imagen con OpenCV: {e}")

    else:
        print("Biblioteca no válida. Seleccione PIL, Matplotlib o OpenCV.")

if __name__ == "__main__":
    main()