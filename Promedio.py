nota1 = int (input("Ingrese nota 1: "))
nota2 = int (input("Ingrese nota 2: "))
nota3 = int (input("Ingrese nota 3: "))
nota4 = int (input("Ingrese nota 4: "))

promedio = (nota1 + nota2 + nota3 + nota4)/4
print (promedio)

if promedio > 89 and promedio < 101 :
    print("A")
elif promedio > 79 and promedio < 90 :
    print("B")
elif promedio > 69 and promedio < 80 :
    print("C")
elif promedio > 59 and promedio < 70 :
    print("D")
elif promedio >= 0 and promedio < 60 :
    print("E")
    
    
    
    

