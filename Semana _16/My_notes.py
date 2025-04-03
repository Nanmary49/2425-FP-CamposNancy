# Escritura de Archivo de Texto
# Se crea un archivo llamado 'my_notes.txt' y se escriben tres líneas en él
with open("my_notes.txt", "w") as file:
    file.write("Primera nota personal.\n")
    file.write("Segunda nota personal.\n")
    file.write("Tercera nota personal.\n")

# Lectura de Archivo de Texto
# Se abre el archivo 'my_notes.txt' en modo lectura y se leen las líneas
with open("my_notes.txt", "r") as file:
    # Leer línea por línea y mostrar en la consola
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea adicionales

# El archivo se cierra automáticamente gracias al uso de 'with open'
