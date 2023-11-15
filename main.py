

def main():
    pass
def calcolatrice():
    domanda = input("che operazione desideri effettuare? rispondi utilizzando i seguenti operatori (+  -  /  * )\n" )
    a = int(input("inserici il primo valore \n"))
    b = int(input("inserici il secondo valore \n"))
    risultato = 0

    def somma (a,b):
        return a+b

    def sottrazione(a,b):
        return a-b

    def moltiplicazione (a,b):
        return a*b

    def divisione (a,b):
        return a/b

    # stampa risultati
    if domanda == "+":
        risultato= somma(a,b)

    elif domanda == "-":
        risultato= sottrazione(a,b)

    elif domanda == "*":
        risultato = moltiplicazione(a, b)

    elif domanda == "/":
        risultato = divisione(a, b)

    print(risultato)

# execute
if __name__ == "__main__":
    calcolatrice()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
