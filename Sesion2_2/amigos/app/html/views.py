from flask import render_template, request, redirect, url_for
from . import html
from ..models import Amigo
from .. import db

@html.route("/amigos", methods=["GET", "POST"])
def tabla_amigos():
    # Si llega un POST, es que el usuario ha rellenado el formulario de "Añadir"
    if request.method == "POST":
        nuevo = Amigo(
            name=request.form["name"],
            lati=request.form["lati"],
            longi=request.form["longi"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for("html.tabla_amigos"))
    
    # Si llega un GET normal, mostramos la tabla
    amigos = Amigo.query.all()
    return render_template("tabla_amigos.html", amigos=amigos)

@html.route("/amigos/borrar/<int:id>")
def borrar_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    db.session.delete(amigo)
    db.session.commit()
    return redirect(url_for("html.tabla_amigos"))

@html.route("/amigos/modificar/<int:id>", methods=["GET", "POST"])
def modificar_amigo(id):
    amigo = Amigo.query.get_or_404(id)
    
    if request.method == "POST":
        amigo.name = request.form["name"]
        amigo.lati = request.form["lati"]
        amigo.longi = request.form["longi"]
        db.session.commit()
        return redirect(url_for("html.tabla_amigos"))
        
    return render_template("modificar_amigo.html", amigo=amigo)