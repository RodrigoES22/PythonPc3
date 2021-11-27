import random
def ale():
    lista = random.sample(range(0,100),20)
    print(f"Su lista es la siguiente:\n {lista}")
    lista.sort()
    print(f"Su lista ordenada de menor a mayor es la siguiente:\n {lista}")