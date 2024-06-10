import fuzzing

print("Digite la URL a realizar fuzzing")
url = input()

print("Seleccione el tipo de fuzzing a realizar\n1. Comun\n2. SQLI\n3. Extencion de archivos")
tipo = input()
tipo = int(tipo)

match tipo:
    case 1:
        fuzzing.fuzzingSearchCommon(url) 
    case 2:
        fuzzing.fuzzingSearchDB(url)
    #case 3:
        #fuzzing.fuzzingSearhExt(url)
    case other:
        print("Seleccione una opcion valida")
