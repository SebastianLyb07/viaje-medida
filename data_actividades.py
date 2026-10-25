"""Actividades. dificultad/edad_minima/incluye: None si no aplica."""
_T = [  # destino, nombre, horas, precio, dificultad, edad_minima, incluye
    ("kioto", "Ceremonia del Té en Gion", 2, 30, None, None, "Degustación de dulces tradicionales matcha"),
    ("kioto", "Tour Nocturno por Fushimi Inari", 3, 40, "media", 10, None),
    ("kioto", "Clase de Cocina Ramen y Gyozas", 3, 65, None, 12, "Ingredientes, delantal y recetario impreso"),
    ("kioto", "Ruta en Bicicleta por el Bosque de Bambú", 4, 50, "baja", None, "Bicicleta eléctrica y casco"),
    ("zanzibar", "Ruta de las Especias y Paseo en Dhow", 5, 45, "baja", None, "Almuerzo tradicional especiado"),
    ("zanzibar", "Snorkel en el Atolón Mnemba", 4, 60, "media", 8, "Tubo, gafas y aletas"),
    ("zanzibar", "Visita Guiada por Stone Town", 2, 20, None, None, None),
    ("playa-del-carmen", "Buceo en Cenotes Sagrados", 4, 75, "alta", 16, "Bombona de oxígeno, linterna subacuática y neopreno"),
    ("playa-del-carmen", "Excursión a las Ruinas de Tulum", 6, 55, "baja", None, "Entradas al recinto y transporte en autobús"),
    ("playa-del-carmen", "Paseo en Catamarán al Atardecer", 3, 65, None, 18, "Barra libre de bebidas y aperitivos"),
]
ACTIVIDADES = [dict(id=i, destino=d, nombre=n, horas=h, precio=p, dificultad=df, edad_minima=em, incluye=inc)
               for i, (d, n, h, p, df, em, inc) in enumerate(_T, start=1)]
