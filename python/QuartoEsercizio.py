#creare un programma che chiede N>= elementi interi all'utente 
# 1. visualizza i numeri pari preceduti dal messaggio "numeri pari sono x"
# 2. visualizza i numeri dispari preceduti dal messaggio "numeri dispari sono y"
# 3. visualizza i numeri in posizione pari, preceduti dal messaggio "numero posizione pari sono z"
# 4. visualizza i numeri in posizione dispari, preceduti dal messaggio "numero posizione dispari sono j"
# 5. visualizza l'array ordinato in modo crescete

#ANALISI


# 1. fase di input: CHIEDERE quanti numeri
# 2. fase di input: chiedere i numeri (lista)
# 3. fase di elaborazione: leggere lista numeri e per ogni elemento controllare resto div 2 = 0 --> numero pari --> memorizzare lista pari 
# 4. fase di elaborazione: leggere lista numeri e per ogni elemento controllare resto div 2 != 0 --> numero dispari --> memorizzare lista dispari 
# 5. se posizione elemento div 2 = 0 --> numero pos dispari --> memorizzare lista pos dispari
# 6. se posizione elemento div 2 !0 --> numero pos pari --> memorizzare lista pos pari
# 7. ordinare i numeri
# 8. stampare 5 pari, dispari, pos pari, pos dispari, numeri (crescente)

#dichiarazione  risorse i/o
#lista numeri, pari, dispari, pos pari, pos dispari
numeri = []
pari = []
dispari = []
pos_pari = []
pos_dispari = []

#fase di input
  
N = int(input("quanti numeri vuoi inserire?")) # n variabile, di INTeri, input, e output stringa
while N <2 :
    print("errore")
    N = int(input("quanti numeri vuoi inserire?"))

for i in range(N):
    numero = int(input("inserisci numero: ")) #richiesta dell input
    numeri.append(numero) #aggiungi il numero alla lista

#fase di elaborazione 

for i in range(N):
    resto = numeri[i] % 2
    if resto == 0:
        pari.append(numeri[i])
    else:
        dispari.append(numeri[i])

# determino la posizione partendo da 1: posizione 1 = primo elemento
for i in range(N):
    if (i + 1) % 2 == 0:
        # posizione pari
        pos_pari.append(numeri[i])
    else:
        # posizione dispari
        pos_dispari.append(numeri[i])

#fase di output
print(f"numeri pari sono {pari}")
print(f"numeri dispari sono {dispari}")

print(f"numero posizione pari sono {pos_pari}")
print(f"numero posizione dispari sono {pos_dispari}")

numeri.sort() #sort = ordinamento crescente
print(numeri) #stampa ordinati

 