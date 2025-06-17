#crear una funcion contar_ocurrencias (palabras)
#que reciba una lista de palabras y retorne un diccionario con el conteo de cada uno

def contar_ocurrencias (palabras):
    conteo = {}
    for palabras in palabras:
        conteo[palabras] = conteo.get(palabras ,0)+1
#defino el diccionario
    return conteo

    
def main():
    lista_palabras = [ "hola", "hola", "hola", "dos", "uno", "dos", "holamundo"]
    resultado= contar_ocurrencias(lista_palabras)
    print(resultado)
if __name__ == "__main__":
    main()
