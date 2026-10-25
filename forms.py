from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange

ENTORNOS = [("", "Cualquiera"), ("playa", "Playa"), ("montaña", "Montaña"), ("ciudad", "Ciudad")]
TIPOS = [("", "Cualquiera"), ("hotel", "Hotel"), ("hostal", "Hostal"), ("cabaña", "Cabaña"), ("apartamento", "Apartamento")]
_PRECIO = [NumberRange(min=1, max=5000, message="Introduce un precio entre 1 y 5000 €.")]


class _Base(FlaskForm):
    class Meta:
        csrf = False  # formulario solo de consulta, sin control de acceso


class ExploradorDestinosForm(_Base):
    entorno = SelectField("Entorno", choices=ENTORNOS, validators=[Optional()])
    sin_visado = BooleanField("Solo destinos sin visado")


class ComparadorAlojamientosForm(_Base):
    precio_max = IntegerField("Presupuesto máximo por noche (€)", validators=[DataRequired("Indica un presupuesto.")] + _PRECIO)
    tipo = SelectField("Tipo de alojamiento", choices=TIPOS, validators=[Optional()])
    desayuno = BooleanField("Desayuno incluido")
    mascotas = BooleanField("Admite mascotas")


class ViajeAMedidaForm(_Base):
    entorno = SelectField("Entorno", choices=ENTORNOS, validators=[Optional()])
    sin_visado = BooleanField("Viajar sin visado")
    tipo = SelectField("Tipo de alojamiento", choices=TIPOS, validators=[Optional()])
    precio_max = IntegerField("Gasto máximo por noche (€)", validators=[DataRequired("Indica un gasto máximo.")] + _PRECIO)
    desayuno = BooleanField("Desayuno incluido")
