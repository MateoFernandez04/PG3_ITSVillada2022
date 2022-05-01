f = open ('holamundo.txt','w')
try:
    f.write(1)
except TypeError:
    print("No se puede escribir en el archivo correspondiente")
