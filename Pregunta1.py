## Problema 1
    # Escriba una función que, dado un string, retorne la longitud de la última palabra. 
    # Se considera que las palabras están separadas por uno o más espacios. 
    # También podría haber espacios al principio o al final del string pasado por 
    # parámetro.
#Función
def lenUltimaPalabra(frase):
   if len(frase)==0:
       return 0
   cantidad=0
   for i in range(len(frase)):
       if frase[i]!=' ':
           cantidad+=1
       else:
           if i<len(frase)-1 and frase[i+1]!=' ':
               cantidad=0
   return cantidad
#Programa
palabra = input("Introduce un string: ")
print(f"La longitud de la última palabra es: {lenUltimaPalabra(palabra)}")
