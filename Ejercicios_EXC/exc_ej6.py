import mysql.connector

############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
conexion1 = mysql.connector.connect(host='localhost',user='matfer',password="cyngaruda2605")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()   