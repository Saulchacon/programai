for i in range(5):
    #[0,1,2,3,4]
    print(f"Hola! Esta es la vuelta {i}");

print("*"*30);

for i in range (55,65):
    #[55,56,57,58,59,60,61,62,63,64]
    print(f"Hola! Esta es la vuelta {i}");

print("*"*30);

for i in range(70,90,3):
    #[70,73,76,79,82,85,88]
    print(f"Hola! Esta es la vuelta {i}");

print("*"*30);

# Break y continue
for i in range (5):
    if(i==3):
        continue;

    print(f"Hola! Esta es la vuelta {i}");

# Texto son iterables
frase = "Hola buenos días sección 005D. Ustedes son lo mejor!!"

for letra in frase:
    print(letra);

print("*"*30);

for i in range (2,101,2):
    print(i);

print("*"*30);

for i in range (1,101):
    if(i % 2 == 0):
        print(i);

print("*"*30);

num = int(input("Ingrese un número: "));

for i in range (1,13):
    print(f"{i} x {num} = {num*i}");

print("*"*30);

for i in range (1,11):
    print(f"Esta es la tabla de multiplicar del número: {i}");

    for j in range (1,13):
        print(f"{i} x {j} = {j*i}");

print("*"*30);

frase = (input("Ingrese una frase: "));

# Contadores 
 
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in frase.lower():
    if (letra == "a"):
        a += 1;
    elif(letra == "e"):
        e += 1;
    elif(letra == "i"):
        i += 1;
    elif(letra == "o"):
        o += 1;
    elif(letra == "u"):
        u += 1;
# Resultado
print(f"El total de la vocal a presente es de: {a}")
print(f"El total de la vocal e presente es de: {e}")
print(f"El total de la vocal i presente es de: {i}")
print(f"El total de la vocal o presente es de: {o}")
print(f"El total de la vocal u presente es de: {u}")
       





















        






















