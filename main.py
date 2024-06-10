import fuzzing

print("Digite la URL a realizar fuzzing")
url = input()

print("Seleccione el tipo de fuzzing a realizar\n1. Comun (Usa palabras que son comunes para directorios)\n2. SQLI (Para descubrir vulnerabilidades de Inyecciones SQL)\n3. Extencion de archivos (En desarrollo)")
tipo = input()
tipo = int(tipo)

match tipo:
    case 1:
        fuzzing.fuzzingSearchCommon(url) 
    case 2:
        fuzzing.fuzzingSearchDB(url)
    case 3:
        print("Funcion en desarrollo")
        #fuzzing.fuzzingSearhExt(url)
    case other:
        print("Seleccione una opcion valida")
