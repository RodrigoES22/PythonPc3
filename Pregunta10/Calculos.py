##Problema 10
 #Crea el siguiente módulo:
 #El módulo se denominará operaciones.py y contendrá 4 funciones para realizar una 
 #suma, una resta, un producto y una división entre dos números. Todas ellas 
 #devolverán el resultado. En las funciones del módulo deberá de haber tratamiento 
 #e invocación manual de errores para evitar que se quede bloqueada una 
 #funcionalidad, eso incluye:
 #• En caso de que se envíen valores a las funciones que no sean números, deberá
 #aparecer un mensaje que informe Error: Tipo de dato no válido.
 #• En caso de realizar una división por cero, deberá aparecer un mensaje que informe
 #Error: No es posible dividir entre cero.
 #Una vez creado el módulo, crea un script calculos.py en el mismo directorio en 
 #el que deberás importar el módulo y ejecutar las funciones

# librerias propias
import operaciones

# Funciones y/o clases
def main():
    print("Bienvenido al menú interactivo")
    while True:
        print("""¿Qué quieres hacer? Escribe una opción
        1) Sumar dos números
        2) Restar dos números
        3) Multiplicar dos números
        4) Dividir dos números
        5) Salir""")

        opcion = input()
        if opcion == '1':
            operaciones.sumar()
        elif opcion == '2':
            operaciones.restar()
        elif opcion =='3':
            operaciones.multiplicacion()
        elif opcion =='4':
            operaciones.division()
        elif opcion =='5':
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break
        else:
            print("Comando desconocido, vuelve a intentarlo")
            return main()

# mi programa  
main()