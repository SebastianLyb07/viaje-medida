from flask import Flask, render_template, request, abort
import services as s
from forms import ExploradorDestinosForm, ComparadorAlojamientosForm, ViajeAMedidaForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-no-csrf"


@app.route("/")
def inicio():
    return render_template("inicio.html", totales=s.contar_catalogo())


@app.route("/acerca")
def acerca():
    return render_template("acerca.html")


@app.route("/destinos")
def lista_destinos():
    return render_template("lista.html", titulo="Destinos", tipo="destino",
                           items=s.get_destinos(), nombre_destinos={})


@app.route("/alojamientos")
def lista_alojamientos():
    return render_template("lista.html", titulo="Alojamientos", tipo="alojamiento", items=s.get_alojamientos())


@app.route("/actividades")
def lista_actividades():
    items = [dict(a, destino_nombre=s.get_destino(a["destino"])["nombre"]) for a in s.get_actividades()]
    return render_template("lista.html", titulo="Actividades", tipo="actividad", items=items)


def _buscar(form_cls, titulo, tipo, buscar):
    """Valida con WTForms (GET) y delega la búsqueda; sin parámetros solo muestra el formulario."""
    form = form_cls(request.args)
    resultados = None
    if request.args and form.validate():
        resultados = buscar(form.data)
    return render_template("buscar.html", titulo=titulo, tipo=tipo, form=form, resultados=resultados)


@app.route("/explorador")
def explorador():
    return _buscar(ExploradorDestinosForm, "Explorador de Destinos", "destino",
                   lambda d: s.filtrar_destinos(d["entorno"], d["sin_visado"]))


@app.route("/comparador")
def comparador():
    def f(d):
        res = s.filtrar_alojamientos(d["precio_max"], d["tipo"], d["desayuno"], d["mascotas"])
        return [dict(a, destino_nombre=s.get_destino(a["destino"])["nombre"]) for a in res]
    return _buscar(ComparadorAlojamientosForm, "Comparador de Alojamientos", "alojamiento", f)


@app.route("/viaje-a-medida")
def viaje_a_medida():
    return _buscar(ViajeAMedidaForm, "Asistente de Viaje a Medida", "combo",
                   lambda d: s.viaje_a_medida(d["entorno"], d["sin_visado"], d["tipo"], d["precio_max"], d["desayuno"]))


@app.route("/destino/<slug>")
def destino(slug):
    d = s.get_destino(slug) or abort(404)
    return render_template("destino.html", d=d, alojamientos=s.alojamientos_de(slug), actividades=s.actividades_de(slug))


@app.route("/alojamiento/<int:id_>")
def alojamiento(id_):
    a = s.get_alojamiento(id_) or abort(404)
    return render_template("alojamiento.html", a=a, d=s.get_destino(a["destino"]))


@app.route("/actividad/<int:id_>")
def actividad(id_):
    a = s.get_actividad(id_) or abort(404)
    return render_template("actividad.html", a=a, d=s.get_destino(a["destino"]))


@app.errorhandler(404)
def no_encontrado(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
