#dati due numeri interi fare
 #la somma
 #la sottrazione (risultato positivo) del primo meno il secondo
 #la molptiplicazione
 #la divisione (se dividi per 0, vis messaggio impossibile)
 #la media
 #il resto della divisione
 #il quoziente della divisione
 #visualizzare il tutto in output

#analisi:
# 1. fase di input controllato --> richiedere i due numeri interi, il primo numero maggiore del sec
# 2. fase di elaborazione --> fare tutte le operazioni
# 3. fase di output --> stampare le operazioni

num1 = 0 #variabile di input
num2 = 0
somma = 0 #risultato fornito
sottrazione = 0
moltiplicazione = 0
divisione = 0 
resto = 0 
media = 0
quoziente = 0

#fase di input 
num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero piu' piccolo del primo: "))

#fase di elaborazione 
while num1 <= num2:
    num2 = int(input("hai inserito il secondo più grande del primo, inserisci di nuovo: "))
somma = num1+num2
sottrazione = num1-num2
moltiplicazione = num1*num2
media = somma/2

if (num2!=0): 
    divisione = num1/num2
    resto = num1%num2
    quoziente = num1//num2
    print("ecco tutte le operazioni:", f"\n  somma = {somma}\n  sottrazione = {sottrazione}\n  moltiplicazione = {moltiplicazione}\n  divisione = {divisione}\n  resto = {resto}\n  quoziente = {quoziente}\n  media = {media}\n")    
else:print("ecco tutte le operazioni:", f"\n  somma = {somma}\n  sottrazione = {sottrazione}\n  moltiplicazione = {moltiplicazione}\n  divisione = {"impossibile"}\n  resto = {"impossibile"}\n  quoziente = {"impossibile"}\n  media = {media}\n")

#la f prende le variabili all interno delle parentesi graffe e non come stringhe