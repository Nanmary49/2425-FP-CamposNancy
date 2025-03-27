# Crear un diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Ascubi",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y modificar el valor de la clave "ciudad"
# Se actualiza la ciudad en el diccionario
informacion_personal["ciudad"] = "Guayaquil"

# Agregar una nueva clave-valor para la "profesion"
# Se actualiza la profesión de la persona en el diccionario
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si la clave "telefono" existe, si no, agregarla
# Se verifica si la clave 'telefono' está presente, si no, se agrega con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad"
# Se elimina la clave 'edad' ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)
