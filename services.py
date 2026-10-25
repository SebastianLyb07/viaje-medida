"""Funciones de acceso y filtrado. Las plantillas nunca recorren los datos en bruto."""
from data_destinos import DESTINOS
from data_alojamientos import ALOJAMIENTOS
from data_actividades import ACTIVIDADES


def _por_id(lista, id_):
    return next((x for x in lista if x["id"] == id_), None)


def contar_catalogo():
    return dict(destinos=len(DESTINOS), alojamientos=len(ALOJAMIENTOS), actividades=len(ACTIVIDADES))


def get_destinos(): return list(DESTINOS)
def get_alojamientos(): return list(ALOJAMIENTOS)
def get_actividades(): return list(ACTIVIDADES)


def get_destino(slug): return next((d for d in DESTINOS if d["slug"] == slug), None)
def get_alojamiento(id_): return _por_id(ALOJAMIENTOS, id_)
def get_actividad(id_): return _por_id(ACTIVIDADES, id_)


def alojamientos_de(slug): return [a for a in ALOJAMIENTOS if a["destino"] == slug]
def actividades_de(slug): return [a for a in ACTIVIDADES if a["destino"] == slug]


def filtrar_destinos(entorno=None, sin_visado=False):
    return [d for d in DESTINOS
            if (not entorno or d["entorno"] == entorno) and (not sin_visado or not d["visado"])]


def filtrar_alojamientos(precio_max=None, tipo=None, desayuno=False, mascotas=False, destinos=None):
    return [a for a in ALOJAMIENTOS
            if (precio_max is None or a["precio"] <= precio_max)
            and (not tipo or a["tipo"] == tipo)
            and (not desayuno or a["desayuno"])
            and (not mascotas or a["mascotas"])
            and (destinos is None or a["destino"] in destinos)]


def viaje_a_medida(entorno=None, sin_visado=False, tipo=None, precio_max=None, desayuno=False):
    """Combinaciones (destino, alojamiento) que cumplen todos los requisitos."""
    out = []
    for d in filtrar_destinos(entorno, sin_visado):
        for a in filtrar_alojamientos(precio_max, tipo, desayuno, destinos=[d["slug"]]):
            out.append((d, a))
    return out
