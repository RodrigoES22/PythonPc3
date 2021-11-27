def sumar():
    try:
        a  =  int(input("Introduce un numero: "))
        b  =  int(input("Introduce otro numero: ")) 
    except:
        print("Tipo de dato no válido")
        return sumar()
    print(f"La suma es: {a+b}")      

def restar():
    try:
        a  =  int(input("Introduce un numero: "))
        b  =  int(input("Introduce otro numero: ")) 
    except:
        print("Tipo de dato no válido")
        return restar()
    print(f"La resta es: {a-b}")      

def multiplicacion():
    try:
        a  =  int(input("Introduce un numero: "))
        b  =  int(input("Introduce otro numero: "))
    except:
        print("Tipo de dato no válido")
        return multiplicacion()
    print(f"La multipliación es: {a*b}")     

def division():
    try:
        a  =  int(input("Introduce un numero: "))
        b  =  int(input("Introduce otro numero: ")) 
    except:
        print("Tipo de dato no válido")
        return division()
    try:
        print(f"La división es: {a/b}")
    except:
        print("Error: No es posible dividir entre cero.")
        return division()        