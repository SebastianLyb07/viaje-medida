"""Destinos. Campos opcionales: consejo, imagen (None si no aplica)."""
DESTINOS = [
    dict(slug="kioto", nombre="Kioto", pais="Japón", entorno="ciudad", temporada_alta="primavera",
         visado=False, imagen=None,
         consejo="La moneda local es el yen y recomendamos llevar siempre efectivo para el acceso a los templos tradicionales."),
    dict(slug="islas-lofoten", nombre="Islas Lofoten", pais="Noruega", entorno="montaña", temporada_alta="invierno",
         visado=False, imagen=None,
         consejo="Es imprescindible viajar con ropa térmica extrema y calzado impermeable."),
    dict(slug="zanzibar", nombre="Zanzíbar", pais="Tanzania", entorno="playa", temporada_alta="verano",
         visado=True, imagen=None, consejo=None),
    dict(slug="playa-del-carmen", nombre="Playa del Carmen", pais="México", entorno="playa", temporada_alta="verano",
         visado=False, imagen=None,
         consejo="La moneda es el peso mexicano, aunque aceptan dólares en casi todas las zonas turísticas."),
]
