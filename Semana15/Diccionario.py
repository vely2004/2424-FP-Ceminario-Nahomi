informacion_personal= { "nombre": "Daina Vega",
"edad":"25 años",
"ciudad":"Arenillas",
"Profesión": "Doctora"}
#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"]= "Guayaquil"
# Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["Profesión"]= "Enfermera"
#Verifica si la clave "telefono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.
if "teléfono" not in informacion_personal:
    informacion_personal["teléfono"]= "0980596384"
#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.
del informacion_personal ["edad"]
print(informacion_personal)


