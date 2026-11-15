from flask import jsonify
from . import api
from ..models import Amigo
from flask import request, abort

@api.route("/amigos", methods=["POST"])
def new_amigo():
    if not request.json:
        abort(422, "No se ha enviado JSON")
    
    name = request.json.get("name")
    if not name:
        abort(422, "El JSON no incluye el campo 'name'")
        
    amigo = Amigo.query.filter_by(name=name).first()
    if amigo:
        abort(422, "Ya existe un amigo con ese nombre")
        
    lati = request.json.get("lati", "0")
    longi = request.json.get("longi", "0")
    device = request.json.get("device", "")
    
    nuevo_amigo = Amigo(name=name, lati=lati, longi=longi, device=device)
    from .. import db
    db.session.add(nuevo_amigo)
    db.session.commit()
    
    return jsonify({"id": nuevo_amigo.id, "name": nuevo_amigo.name, "lati": nuevo_amigo.lati, "longi": nuevo_amigo.longi, "device": nuevo_amigo.device})

@api.route("/amigos", methods=["GET"])
def get_amigos():
    amigos = Amigo.query.all()
    # Convertimos la lista de objetos a un diccionario JSON
    datos = [{"id": a.id, "name": a.name, "lati": a.lati, "longi": a.longi} for a in amigos]
    return jsonify(datos)

@api.route("/amigo/<int:id>", methods=["PUT"])
def edit_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    if not request.json:
        abort(422, "No se ha enviado JSON")
        
    name = request.json.get("name")
    lati = request.json.get("lati")
    longi = request.json.get("longi")
    device = request.json.get("device")
    
    if name: amigo.name = name
    if lati: amigo.lati = lati
    if longi: amigo.longi = longi
    # El device puede venir vacío, por lo que lo actualizamos si está en el JSON explícitamente
    if "device" in request.json: 
        amigo.device = request.json.get("device") or ""
        
    db.session.commit()
        
    return jsonify({"id": amigo.id, "name": amigo.name, "lati": amigo.lati, "longi": amigo.longi, "device": amigo.device})

@api.route("/devices", methods=["GET"])
def get_devices():
    # Obtener todos los amigos que tengan un device definido y no vacío
    amigos = Amigo.query.filter(Amigo.device != None, Amigo.device != "").all()
    # Solo retornamos la lista de strings con los dispositivos
    lista_dispositivos = [a.device for a in amigos]
    return jsonify(lista_dispositivos)