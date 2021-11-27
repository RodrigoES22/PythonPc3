##Problema 2
 #Escriba una función la cual recibe un string y lo retorna convirtiendo la primera 
 #letra de cada palabra a mayúscula y las demás letras a minúscula, dejando inalterados 
 #los demás caracteres. Precondición: el separador de palabras es el espacio: " ".
#Función
def titulo(cadena):
    nueva=""
    inicioPalabra=True              
    for caracter in cadena:
        if not caracter.isalpha():
            nueva+=caracter
            inicioPalabra=True
        else:
            if inicioPalabra:
                nueva+=caracter.upper()
                inicioPalabra=False   
            else:
                nueva+=caracter.lower()
    return nueva
#Programa
mayuscula = input("Introduce un string: ")
print(titulo(mayuscula))
     