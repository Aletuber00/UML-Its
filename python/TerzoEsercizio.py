# Program to read n numbers and display the largest and smallest

def main():
    try:
        n = int(input("Quanti numeri vuoi inserire? "))
    except ValueError:
        print("Per favore inserisci un numero intero.")
        return

    if n <= 0:
        print("Devi inserire almeno un numero.")
        return

    numeri = []
    for i in range(n):
        while True:
            try:
                val = float(input(f"Numero {i+1}: "))
                numeri.append(val)
                break
            except ValueError:
                print("Input non valido, riprova.")

    massimo = max(numeri)
    minimo = min(numeri)

    print(f"Il valore più grande è: {massimo}")
    print(f"Il valore più piccolo è: {minimo}")


if __name__ == "__main__":
    main()
