from flask import Flask

# Flask-App erstellen
app = Flask(__name__)
app.secret_key = "supersecretkey"

# Importiere die Routen
from app import routes
