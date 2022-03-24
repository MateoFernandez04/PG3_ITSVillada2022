palabra= input("Ingrese la palabra que desea evaluar: ")

def verificador(texto):
    igual, aux = 0, 0
    for ind in reversed(range(0, len(texto))):
        if texto[ind].lower() == texto[aux].lower():
            igual += 1
        aux += 1
    if len(texto) == igual:
        frase=("es palindromo!")
    else:
        frase=("no es palindromo!")
    return frase
print("El texto",verificador(palabra))