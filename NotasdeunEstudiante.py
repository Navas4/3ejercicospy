
def calcular_media(puntuaciones):
    
    if len(puntuaciones) != 4:
        raise ValueError("Debe ingresar exactamente 4 puntuaciones.")
    
    
    media = sum(puntuaciones) / len(puntuaciones)
    
    return media

def main():
    
    puntuaciones = []
    
    for i in range(4):
        while True:
            try:
                puntuacion = int(input(f"Introduce la puntuación {i+1} (entre 0 y 100): "))
                if 0 <= puntuacion <= 100:
                    puntuaciones.append(puntuacion)
                    break
                else:
                    print("La puntuación debe estar entre 0 y 100. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número entero.")
    
   
    media = calcular_media(puntuaciones)
    
    
    print(f"La media de las puntuaciones es: {media:.2f}")

if __name__ == "__main__":
    main()
