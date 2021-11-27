import random
b = random.randint(1,100)
def alea():
    try:
        a = int(input("Digite un número: "))
        if b < a:
            print("El número es inferior al digitado")
            return alea()      
        elif b > a:
            print("El número es superior al digitado")
            return alea()    
        else:
            print("GANASTE!!!")        
    except:
        print("ERROR")
        return alea()    