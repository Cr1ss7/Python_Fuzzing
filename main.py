import fuzzing
import sys 

try:
    print("Digite la URL a realizar fuzzing")
    url = input()

    print("Seleccione el tipo de fuzzing a realizar\n1. Comun (Usa palabras que son comunes para directorios)\n2. SQLI (Para descubrir vulnerabilidades de Inyecciones SQL)\n3. Seleccion propia de diccionario")
    tipo = input()
    tipo = int(tipo)

    match tipo:
        case 1:
            fuzzing.fuzzingSearchCommon(url) 
        case 2:
            fuzzing.fuzzingSearchDB(url)
        case 3:
            print("Digite la direccion de el diccionario a emplear")
            dirb = input()
            fuzzing.fuzzingSelected(url,dirb)
        case other:
            print("Seleccione una opcion valida")
#Funciuon para interrumpir la aplicacion
except KeyboardInterrupt:
    print("Saliendo de la aplicacion...")
    sys.exit()

