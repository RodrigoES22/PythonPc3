##Problema 3
 #Definir una clase llamada “CIRCULO” que puede ser construida por un atributo radio. 
 #La clase “CIRCULO” debe tener un método que puede calcular el área en utilizando el 
 #atributo radio
#Librerías
import math
#Clase y Función:
class CIRCULO:
    def radio(self):
        r = int(input("Ingrese el radio del círculo: "))
        try:
            while r<0:
                print('El radio debe ser mayor o igual a 0')
                q = input('¿Desea convertir dicho número a positivo y operar con él? (si/no): ')
                if q.lower() == 'si':
                    r = abs(r)
                    return f"El área del círculo es: {math.pi*r}"
                elif q.lower() == 'no': 
                    print("--Volverá al inicio--")
                    return CIRCULO.radio(self)
                else:
                    print("--Comando no permitido, volverá al inicio--")
                    return CIRCULO.radio(self)    
            return f"El área del círculo es: {math.pi*r}"
        except:
            print("Ha ocurrido un error, introduce bien el número")
            return CIRCULO.radio(self)
#Programa:
R = CIRCULO()
R.radio()