# 1. popolare un array di N elementi interi, quindi chiedere un numero intero e visualizzare se è presente o meno
#se è presente indicare quante volte è presente e le posizioni in cui è presente

#analisi dei requisiti

#risorse: array di N elementi interi, numeri interi

#richiesta: visualizzare se il numero inserito é presente o meno

n=0
# 1. PREPARAZIONE: chiediamo la dimensione N
while True:
    n = int(input("quanti numeri vuoi inserire?"))
    if n>0:
        break
    print("per favore, inserisci un numero maggiore di 0: ")

# 2. POPOLAMENTO: riempiamo la lista
numeri = []
for i in range (n):
    valore = int (input("inserisci un numero: "))
    numeri.append(valore) #aggiungiamo il numero alla lista

# 3. RICERCA: chiediamo cosa cercare e analizziamo la lista
while True:
    bersaglio = int(input("che numero vuoi cercare?"))
    conteggio = 0
    posizioni = []
    for i in range (len(numeri)):  #len(numeri) ci dice quanto é lunga la lista
        if numeri[i] == bersaglio:
            conteggio = conteggio +1
            posizioni.append(i+1)

    if conteggio == 0:
        print(f"il numero {bersaglio} non e' presente nella lista.")
    else:
        print(f"il numero {bersaglio} é presente")
        print(f"appare {conteggio} volta/e")
        print(f"si trova nelle seguenti posizioni: {posizioni}°")
        break
