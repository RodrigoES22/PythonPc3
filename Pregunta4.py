##Problema 4
 #Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos 
 #largo y ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área 
 #utilizando los atributos de la clase.
#Clase y Función:
class RECTANGULO:
    def rect(self,largo,ancho):
        self.largo = largo
        self.ancho = ancho
        print(f'El largo del rectángulo es {self.largo} y el ancho es {self.ancho}')
    def resul(self):           
        return f'El área es: {self.largo*self.ancho}'
#Programa:
l = float(input("Digite el largo: "))
a = float(input("Digite el ancho: "))
R = RECTANGULO()
R.largo = l
R.ancho = a
R.resul()