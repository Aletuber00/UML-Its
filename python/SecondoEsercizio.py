import sys

stringa     = "ciao" 
intero      = 3
reale       = 2.5
realeFinto  = 2,5
booleano    = True

print(f"stringa = {type(stringa)}")   
print(f" intero = {type(intero)}")
print(f" reale = {type(reale)}")
print(f" realeFinto = {type(realeFinto)}")
print(f" booleano = {type(booleano)}")

print(f"dimensione stringa = {sys.getsizeof(stringa)}")
print(f"dimensione intero = {sys.getsizeof(intero)}")
print(f"dimensione reale = {sys.getsizeof(reale)}")
print(f"dimensione realeFinto = {sys.getsizeof(realeFinto)}")
print(f"dimensione booleano = {sys.getsizeof(booleano)}")

#casting (cambio del tipo della variabili)
