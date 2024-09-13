# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (2 semanas)
temperaturas = [
    [   # Ciudad 1
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
    [   # Ciudad 2
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
    [   # Ciudad 3
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

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} °C")