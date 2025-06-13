# programai
mi primera programacionn

def suma(a,b):
    suma = a+b
    return suma

def resta(a,b):
    resta= a-b
    return resta

def division(a,b):
    divison= a/b
    return divison

def multiplicacion(a,b):
    multiplicacion= a * b
    return multiplicacion


a = int(input("ingrese el primer numero"))

b= int(input("ingrese el segundo numero"))


print("1) sumar ")
print("2) Restar ")
print("3) Division")
print("4) Multiplicacion" )

opcion=int(input("ingrese que opcion desea"))



if opcion == 1:
    suma (a+b)
    print("ese es su resultado")