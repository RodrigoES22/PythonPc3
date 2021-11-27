##Problema 5:
 #Cree una clase Alumno e inicialícela con el nombre y el número de registro. 
 # Haga los métodos para:
 # 1. Display - Debe mostrar toda la información del estudiante 
 #    (nombre y número de registro).
 # 2. setAge - Debe asignar la edad al estudiante
 # 3. setNota - Debe asignar las notas al estudiante.

#Clase y función:
class Alumno:
    def Display(self,name,numero):
        self.name = name
        self.numero = numero
        estudiante = {'Nombre':self.name,'Número de registro':self.numero}
        return estudiante
    def setAge(self,edad):
        self.edad = edad
    def setNota(self,notas):
        self.notas = notas 
    def final(self):
        return {'Nombre: ':self.name,'Número de registro: ':self.numero,'Edad: ':self.edad,'Notas: ':self.notas}   
def NOTE():
    a = []
    e = int(input("¿Cuántas notas tiene usted?: "))
    print(f"Agregue los {e} números: ")
    for i in range(len(a),e):
        a.append(int(input()))
    return a    
#Programa:
yo = Alumno()
yo.name = input("Escriba su nombre: ")
yo.numero = input("Digite su número de registro: ")
yo.edad = int(input("Digite su edad: "))
yo.notas = NOTE()
yo.final()