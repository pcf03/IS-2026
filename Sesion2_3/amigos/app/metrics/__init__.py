from flask import Blueprint

# Creo el blueprint "metrics"
metrics = Blueprint("metrics", __name__)

# Importo las vistas al final para evitar importaciones circulares
from app.metrics import views
