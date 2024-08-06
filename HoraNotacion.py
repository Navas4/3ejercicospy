
def convertir_a_12_horas(hora_24):
    
    hora, minuto = map(int, hora_24.split(':'))
    
    
    if hora >= 12:
        periodo = "PM"
    else:
        periodo = "AM"
    
    
    hora_12 = hora % 12
    if hora_12 == 0:
        hora_12 = 12
    
    
    return f"{hora_12}:{minuto:02d} {periodo}"


entrada = input("Introduce la hora en formato de 24 horas (HH:MM): ")
resultado = convertir_a_12_horas(entrada)
print(resultado)
