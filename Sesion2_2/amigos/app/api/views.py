from flask import jsonify
from . import api
from ..models import Amigo

@api.route("/amigos", methods=["GET"])
def get_amigos():
    amigos = Amigo.query.all()
    # Convertimos la lista de objetos a un diccionario JSON
    datos = [{"id": a.id, "name": a.name, "lati": a.lati, "longi": a.longi} for a in amigos]
    return jsonify(datos)