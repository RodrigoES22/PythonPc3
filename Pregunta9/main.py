## Problema 9
 #Realizar el juego de “adivina el numero”. Se deberá crear un módulo que genere un 
 #valor aleatorio entre 1 y 100 y no se muestre. Después solicitar la carga de 
 #valores por teclado de un número y mostrar el mensaje “Has ganado” si el número es 
 #correcto (igual al número aleatorio). En caso contrario mostrar un mensaje 
 #informando si el número aleatorio es superior o inferior al introducido y solicitar 
 #un nuevo número hasta que se logre adivinar. Luego crea un script main.py en el 
 #mismo directorio en el que deberás importar el módulo y ejecutar las funciones.
 #Nota: utilizar el módulo “random” para generar un numero aleatorio.
import aleatorio
print("""Bienvenido al juego 'ADIVINA EL NÚMERO'
    Reglas:
    1) Deberá escribir un número entero del 1 al 100
    2) El objetivo es que adivine el número aleatorio que el programa generó
    3) Dependiendo del número que usted elija y el número que el rograma generó,
       podrá ver mensajes donde se especificará si es mayor o menor
    4) En caso de acertar el número saldrá un mensaje de victoria y el programa 
       se acabará   
    """)
aleatorio.alea() 