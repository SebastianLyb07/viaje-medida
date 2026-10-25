"""Alojamientos. 'destino' referencia el slug del destino. estrellas/extra: None si no aplica."""
_A = [  # destino, nombre, tipo, precio, desayuno, mascotas, estrellas, extra
    ("kioto", "Ryokan Tradicional Gion", "hotel", 140, True, False, 4, "Baño termal privado en la habitación"),
    ("kioto", "Capsule Hostel Urban", "hostal", 35, False, False, 2, None),
    ("kioto", "Apartamento Bambú Arashiyama", "apartamento", 95, False, True, None, "Terraza con vistas al río"),
    ("islas-lofoten", "Rorbu Fjord Cabins", "cabaña", 160, True, True, 4, "Acceso directo al muelle del fiordo"),
    ("islas-lofoten", "Arctic Light Hotel", "hotel", 210, True, False, 5, "Mirador acristalado en la azotea"),
    ("islas-lofoten", "Refugio de Pescadores Svolvær", "hostal", 55, False, True, None, None),
    ("playa-del-carmen", "Hostal Caribe Maya", "hostal", 25, True, True, 2, None),
    ("playa-del-carmen", "Eco-Villas Tulum Road", "cabaña", 110, False, True, 3, "Funciona al 100% con energía solar"),
    ("playa-del-carmen", "Grand Resort Riviera", "hotel", 190, True, False, 5, "Club de playa privado"),
    ("playa-del-carmen", "Loft Quinta Avenida", "apartamento", 80, False, False, None, None),
]
ALOJAMIENTOS = [dict(id=i, destino=d, nombre=n, tipo=t, precio=p, desayuno=b, mascotas=m, estrellas=e, extra=x)
                for i, (d, n, t, p, b, m, e, x) in enumerate(_A, start=1)]
