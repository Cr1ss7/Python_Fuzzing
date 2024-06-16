import requests

def fuzzingSearchCommon(url):
    url = veriUrl(url)
    print("Realizando Fuzzing a -> "+url)
    with open("dirb/big.txt", "r") as tf:
        lines = tf.read().split("\n")

    for line in lines:
        full_url = url+"/"+line
        resp = requests.get(full_url)
        if resp.status_code == 200 or resp.status_code == 201 or resp.status_code == 202 or resp.status_code == 203:
            print(full_url+" -> EXISTENTE")

def fuzzingSearchDB(url):
    url = veriUrl(url)
    print("Realizando Fuzzing a -> "+url)
    with open("dirb/sqli.auth.bypass.txt", "r") as tf:
        lines = tf.read().split("\n")

    for line in lines:
        full_url = url+"/"+line
        resp = requests.get(full_url)
        if resp.status_code == 200 or resp.status_code == 201 or resp.status_code == 202 or resp.status_code == 203:
            print(full_url+" -> EXISTENTE")

def fuzzingSelected(url, dirb):
    url = veriUrl(url)
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
            print(full_url+" -> EXISTENTE")

#Funcion para verificar url
def veriUrl(url):
    if url[-1] == "/":
        url = url[:-1]
    return url

#Diccionarios extraidos de https://github.com/danielmiessler/SecLists/tree/master/Fuzzing
#Diccionarios extraidos de https://github.com/00xBAD/kali-wordlists/