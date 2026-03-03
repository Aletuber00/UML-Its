#funzione che serve a validare nome e cognome secondo i vincoli
from datetime import datetime
import re

def controllo_nome_cognome(stringa_input, messaggio):
    if not stringa_input:  #se non inserisce nulla 
        print(f"errore, {messaggio} sbagliato, campo vuoto")
        return False
    if len(stringa_input)>30 and not(re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"per il {messaggio} accetto massimo 30 caratteri e non sono ammessi numeri")
        return False
    if len(stringa_input)>30 and (re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"per il {messaggio} accetto massimo 30 caratteri")
        return False
    if len(stringa_input)<30 and not(re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"per il {messaggio} inserire solo caratteri e non sono ammessi numeri")
        return False
    if len(stringa_input)<2 and not(re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"per il {messaggio} accetto almeno 2 caratteri e non sono ammessi numeri ")
        return False
    if len(stringa_input)<2 and (re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"per il {messaggio} accetto almeno 2 caratteri")
        return False
    if len(stringa_input)>2 and not (re.match(r"^[A-Za-z]+$", stringa_input)):
        print(f"errore, {messaggio} sbagliato")
        print("inserire solo caratteri")
        return False
    else:
        return True

def controllo_data(data_input):
    try:
        data_inserita=datetime.strptime(data_input,"%d/%m/%Y")  
        anno = data_inserita.year
        anno_corrente = datetime.now().year
        if (anno < 1950 or anno > anno_corrente):
            print("errore, data non valida")
            return False
        else:
            return True
    except ValueError:
        print("formato data non valido")
        return False
    
def controllo_voto_laurea(voto_input):
    try:
        voto = int(voto_input)
        if (voto > 110 or voto <66):
            print("errore, il voto deve essere compreso tra 66 e 110")
            return False
        else:
            return True
    except ValueError:
        print("formato del voto non valido")
        return False        

def controllo_lode(lode_input):
     if not lode_input:  #se non inserisce nulla 
        print(f"errore, campo vuoto")