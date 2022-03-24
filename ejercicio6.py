def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador

print("Coloque un texto")
cadena = input()
cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}'' hay {cantidad} vocales")