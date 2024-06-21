import model.colors as color
import model.fuzzing as fuzzing
import sys 

try:
    print(f"{color.HEADER}Seleccione el tipo de fuzzing a realizar{color.ENDC}\n{color.WARNING}1. Comun (Usa palabras que son comunes para directorios){color.ENDC}\n{color.FAIL}2. SQLI (Se encuentra en desarrollo){color.ENDC}\n{color.WARNING}3. Seleccion propia de diccionario{color.ENDC}")
    tipo = input()
    tipo = int(tipo)

    print(f"{color.OKGREEN}Digite la URL a realizar fuzzing{color.ENDC}")
    if tipo == 1 or tipo == 3:
        print(f"{color.WARNING}Ejemplo: https://example.com/{color.ENDC}")
    elif tipo == 2:
        print(f"{color.WARNING}Ejemplo: https://insecure-website.com/products?category=Gifts{color.ENDC}")
    url = input()

    match tipo:
        case 1:
            fuzzing.fuzzingSearchCommon(url) 
        case 2:
            #print(f"{color.WARNING}Apartado en desarrollo...{color.ENDC}")
            fuzzing.fuzzingSearchDB(url)
        case 3:
            print(f"{color.OKGREEN}Digite la direccion de el diccionario a emplear{color.ENDC}")
            dirb = input()
            fuzzing.fuzzingSelected(url,dirb)
        case other:
            print(f"{color.FAIL}Seleccione una opcion valida{color.ENDC}")

#Funcion para interrumpir la aplicacion
except KeyboardInterrupt:
    print(f"{color.HEADER}Saliendo de la aplicacion...{color.ENDC}")
    sys.exit()

