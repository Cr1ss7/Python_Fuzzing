import requests
import model.colors as c
import webbrowser as wb

#Variable para abrir url en ventana del navegador
def fuzzingSearchCommon(url):
    url = veriUrl(url)
    print("Realizando Fuzzing a -> "+url)
    ourl = openURL()
    if ourl == True:
        print(f"{c.WARNING}[+] ADVERTENCIA:\nSe recomienda abrir una ventana de navegador especifica para el fuzzing\n\nPresiones RETURN o ENTER para proseguir{c.ENDC}")
        input()
    with open("dirb/big.txt", "r") as tf:
        lines = tf.read().split("\n")

    for line in lines:
        full_url = url+"/"+line
        resp = requests.get(full_url)
        if resp.status_code == 200 or resp.status_code == 201 or resp.status_code == 202 or resp.status_code == 203:
            print(f"{c.OKCYAN}"+full_url+f"{c.ENDC}"+f"{c.OKGREEN} -> EXISTENTE{c.ENDC}")
            if ourl == True:
                wb.open(full_url, new=2)

def fuzzingSearchDB(url):
    ourl = openURL()
    if ourl == True:
        print(f"{c.WARNING}[+] ADVERTENCIA:\nSe recomienda abrir una ventana de navegador especifica para el fuzzing\n\nPresiones RETURN o ENTER para proseguir{c.ENDC}")
        input()
    print(f"{c.HEADER}Realizando Fuzzing a -> "+url+f"{c.ENDC}")
    with open("dirb/sqli.auth.bypass.txt", "r") as tf:
        lines = tf.read().split("\n")

    for line in lines:
        full_url = url+line
        resp = requests.get(full_url)
        if resp.status_code == 200 or resp.status_code == 201 or resp.status_code == 202 or resp.status_code == 203:
            print(f"{c.OKCYAN}"+full_url+f"{c.ENDC}"+f"{c.OKGREEN} -> EXISTENTE{c.ENDC}")
            if ourl==True:
                wb.open(full_url, new=2)

def fuzzingSelected(url, dirb):
    url = veriUrl(url)
    ourl = openURL()
    if ourl == True:
        print(f"{c.WARNING}[+] ADVERTENCIA:\nSe recomienda abrir una ventana de navegador especifica para el fuzzing\n\nPresiones RETURN o ENTER para proseguir{c.ENDC}")
        input()
    try:
        with open(dirb, "r") as tf:
            print("Realizando Fuzzing a -> "+url)
            lines = tf.read().split("\n")
    except:
        print(f"Diccionario {dirb} no existente")
        return

    for line in lines:
        full_url = url+"/"+line
        resp = requests.get(full_url)
        if resp.status_code == 200 or resp.status_code == 201 or resp.status_code == 202 or resp.status_code == 203:
            print(f"{c.OKCYAN}"+full_url+f"{c.ENDC}"+f"{c.OKGREEN} -> EXISTENTE{c.ENDC}")
            if ourl==True:
                wb.open(full_url, new=2)

#Funcion para verificar url
def veriUrl(url):
    if url[-1] == "/":
        url = url[:-1]
    return url

def openURL():
    print(f"{c.WARNING}Desea que cada que se encuentre una pagina se abra en el navegador?\n1. Si\n2. No{c.ENDC}")
    i = input()
    if i=="1":
        return True
    else:
        return False
#Diccionarios extraidos de https://github.com/danielmiessler/SecLists/tree/master/Fuzzing
#Diccionarios extraidos de https://github.com/00xBAD/kali-wordlists/