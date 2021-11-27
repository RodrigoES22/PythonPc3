##Problema 7:
 #Escribe una función de Python que imprima las primeras n filas del triángulo de 
 #Pascal. Nota: El triángulo de Pascal es una figura aritmética y geométrica 
 #imaginada por primera vez por Blaise Pascal.
def trianguloPascal(n):
    lista = [[1],[1,1]] 
    for i in range(1,n):
        linea = [1]
        for j in range(0,len(lista[i])-1):
            linea.extend([ lista[i][j] + lista[i][j+1] ])
        linea += [1]
        lista.append(linea)
    return lista
try:
    n = int(input("Numero de lineas para triangulo de Pascal: "))
    resultado = trianguloPascal(n-1)
    for i in resultado:
        print (i)
except:
    print ("Tiene que ser un valor numerico")