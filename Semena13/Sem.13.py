def temperatura_promedio(ciudades_temperaturas, ciudad_idx):
    """
       Calcula la temperatura promedio de una ciudad durante un período de tiempo dado.

       Args:
           ciudades_temperaturas (list): Lista de matrices 3D con los datos de temperaturas para múltiples ciudades.
           ciudad_idx (int): Índice de la ciudad en la lista de temperaturas.

       Returns:
           float: Temperatura promedio de la ciudad seleccionada.
       """
    # Verificar que el índice de la ciudad sea válido
    if ciudad_idx < 0 or ciudad_idx >= len(ciudades_temperaturas):
        return "Índice de ciudad inválido"

    # Datos de ciudad correspondiente
    ciudad_temperaturas = ciudades_temperaturas[ciudad_idx]
    suma_temperaturas = 0
    total_dias = 0

    # Iterar por cada semana de la ciudad
    for semana in ciudad_temperaturas:
        suma_temperaturas += sum([dia["temp"] for dia in semana])
        total_dias += len(semana)

    # Verificar que no se divida por cero
    if total_dias == 0:
        return "No hay datos de temperaturas para la ciudad"

    promedio = suma_temperaturas / total_dias
    return promedio

# Datos
temperaturas = [
    [   # Huaquillas
        [   # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 10},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 20}
        ],
    ],
    [   # Arenillas
        [   # Semana 1
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 25}
        ],
    ],
    [   # Santa_rosa
        [   # Semana 1
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 30},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 20}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 17}
        ],
    ],
]

ciudades = ["Huaquillas", "Arenillas", "Santa_rosa"]
ciudad_idx = int(input("Elige una ciudad según el número (1 - Huaquillas, 2 - Arenillas, 3 - Santa_Rosa): ")) - 1
# Llamar a la función
promedio = temperatura_promedio(temperaturas, ciudad_idx)
print(f"El promedio de temperaturas en {ciudades[ciudad_idx]} es: {promedio:.2f} °C")