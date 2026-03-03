#Popolare un array di N elementi interi quindi chiedere un numero intero e visualizzare tutti gli elementi diversi dal numero inserito.

n=0
# 1. PREPARAZIONE: chiediamo la dimensione N
while True:
    n = int(input("quanti numeri vuoi inserire?"))
    if n>0:
        break
    print("per favore, inserisci un numero maggiore di 0 intero: ")

# 2. POPOLAMENTO: riempiamo la lista
numeri = []
for i in range (n):
    valore = int (input("inserisci un numero: "))
    numeri.append(valore) #aggiungiamo il numero alla lista


# 3. RICERCA: chiediamo cosa cercare
bersaglio = int(input("che numero vuoi scegliere?"))
conteggio = 0
posizioni = []

print(f"ecco i numeri diversi da {bersaglio}: ")
for numero in numeri:
    if numero != bersaglio:
        print(numero)