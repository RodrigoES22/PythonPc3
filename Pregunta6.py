##Pregunta 6:
 #Cree un programa que solicite al usuario una lista de calificaciones separadas 
 #por comas. Divida la cadena en calificaciones individuales y almacénelas en una 
 #lista para luego convertir cada calificación en un entero. Deberá utilizar una 
 #sentencia try/except para informar al usuario cuando los valores introducidos no 
 #puedan ser convertidos debido a un error de tipeo o formato.
#Función:
def Calificaciones():
    a = []
    b = []
    try:
        cantidad = int(input("¿Cuántas notas digitará?: "))
    except:
        print("ERROR")
        return Calificaciones()    
    print(f"Digite las {cantidad} calificaciones: ")
    for i in range(len(a),cantidad):
        try:    
            a.append(float(input("-")))
        except:
            print("ERROR")
            return Calificaciones()   
    print(f"Su lista es la siguiente:{a}")
    for f in a:
        b.append(int(f))
    print(f"Estas son sus notas: {b}")
#Programa:
Calificaciones()