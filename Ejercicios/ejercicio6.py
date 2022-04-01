def contar_vocales(cadena: str):
	contador: int = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

print("Coloque un texto")
cadena: str = input()
cantidad: int = contar_vocales(cadena)
print(f"En la cadena '{cadena}' hay {cantidad} vocales")