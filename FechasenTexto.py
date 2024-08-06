
from datetime import datetime

def convertir_fecha(fecha_texto):
    
    meses = {
        'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
        'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
    }
    
   
    fecha_texto = fecha_texto.replace(',', '').strip()
    
   
    partes = fecha_texto.split()
    
    
    dia = int(partes[0])
    mes_nombre = partes[1]
    año = int(partes[2])
    
    
    mes = meses[mes_nombre]
    
    
    return f"{dia} {mes} {año}"


entrada = "15, Febrero 1989"
resultado = convertir_fecha(entrada)
print(resultado)

    
    
    
    
    
