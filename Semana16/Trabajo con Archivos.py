#Crea un nuevo archivo llamado my_notes.txt.
#Escribe en el archivo
#Se utiliza write() para escribir y llamamos file.close()para cerrar el archivo
file=open("my_notes.txt", "w")
file.write("Hola.\n")
file.write("Hoy aprendí a trabajar con archivos.\n")
file.write("Es importante practicar para aprender.\n")
file.close()
#Abrimos el archivo pero ahora en modo lectura
#Lectura de Archivo de Texto
#Lee el contenido del archivo línea por línea utilizando el método adecuado.
#Utilizamos readline() para leer el archivo línea por línea dentro de un bucle while.
file=open("my_notes.txt", "r")
line=file.readline()
while line:
    print(line.strip())
    line=file.readline()
#Cerramos el archivo
file.close()