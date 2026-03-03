# 4. fare un programma che chiede all' utente:

#Nome				solo caratteri	alfabetici, accento, speciali, NO numeri, NO campo vuoto, min 2 caratteri
				
#Cognome			solo caratteri  alfabetici, accento, speciali, NO numeri, NO campo vuoto, min 2 caratteri

#Data di nascita	data 19/12/2000

#voto di laurea		66/100

#lode				si/no true o false

#stampa 1. visualizzare nome, cognome, 
#stampa 2. visualizzare data di nascita, voto e lode
#stampa 3. visualizzare tutti i dati

#ANALISI DEI REQUISITI
# 1. inserire il nome (con i vincoli)
# 2. inserire il cognome (con i vincoli)
# 3. inserire la data di nascita (con i vincoli)
# 4. inserire il voto di laurea
# 5. inserire se ha preso la lode
# 6. chiedere il tipo di stampa 
# 7. chiedere se vuole inserire un altro studente (se si, visualizzare #1-6)

#definire una classe (modello di dato/i) STUDENTE
#attributi: nome, cognome, data di nascita, voto di laurea, lode
#metodi:    3
#funzioni:  7
from datetime import datetime
import re 
import Controlli


class Studente:
    def __init__(self,nome,cognome,data_nascita): #attributi
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        #self.voto_laurea = voto_laurea
        #self.lode = lode
    def stampa_nome_cognome(self):  #metodi
        print(f"cognome: {self.cognome}, nome: {self.nome}")
    def stampa_cognome_voto_laurea(self):
        print(f"cognome: {self.cognome}, voto di laurea: {self.voto_laurea}")
    def stampa_all(self):
        print(f"nome: {self.nome}, cognome: {self.cognome}, data di nascita: {self.data_nascita}, voto di laurea: {self.voto_laurea}, lode: {self.lode}")
              
#definizione di un ogetto (singoli casi, studenti)
    
while True:
    nome=input("inserisci il nome: ").strip()
    risposta = Controlli.controllo_nome_cognome(nome,"nome")
    if risposta:
        break

while True:
    cognome=input("inserisci il cognome: ").strip()
    risposta = Controlli.controllo_nome_cognome(cognome,"cognome")
    if risposta:
        break

while True:
    data_nascita=input("inserisci la data di nascita: ").strip() #strip toglie gli spazi
    risposta = Controlli.controllo_data(data_nascita)
    if risposta:
        break            

while True:
    try:
        voto = int(input("Inserisci il voto della laurea: ").strip())
        risposta = Controlli.controllo_voto_laurea(voto)
        if risposta:
            break
    except ValueError:
        print("Errore: inserisci un numero valido!")


voto = risposta
risposta1 = "si" or "Si"
risposta2 = "no" or "No"
risposta3 = risposta1 or risposta2

while True:
    if voto == 110:
        risposta3 = input("Con lode o senza? Rispondere con Si o No: ").strip().lower()
    if not risposta3:  #se non inserisce nulla 
        print(f"errore, campo vuoto")
    if risposta3 == risposta1:
        print("Congratulazioni")
    if risposta3 == risposta2:
        print("Pazienza")
    
