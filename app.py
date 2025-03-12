# Autores: Alexis Emmanuel Durán Alberto, Carlos René Andrade De Pro, Jesús David Gutiérrez Carranza, Oswaldo Emmanuel Sierra Castro
# Fecha: 06-03-2025
# Nombre: app.py
# Descripción: Iniciador de todo el proyecto donde se almacenan las rutas y se le da uso a Flask.

from flask import app
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) # ◀ Se inicia el servidor en modo debug para poder ver los errores o cambios en tiempo real.