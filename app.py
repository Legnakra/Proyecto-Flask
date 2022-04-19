#Importar herramientas necesarias de flask
from flask import Flask, render_template, abort

#Importar librería os para emplear environ
import os

#Importar json para lectura de books.json
import json

#Variable app por flask
app = Flask (__name__)

#Leer fichero json
with open("books.json") as fichero:
    datos=json.load(fichero)

#Definir ruta de inicio
@app.route('/')
def inicio():
    return render_template("inicio.html",libros=datos)

#Definir ruta de libro
@app.route('/libro/<isbn>')
def libro(isbn):
    for book in datos:
        if "isbn" in book.keys() and isbn == book["isbn"]:
            return render_template("libro.html",libro=book)
    abort(404)

#Definir ruta de categoria
@app.route('/categoria/<categoria>')
def categoria(categoria):
    for category in datos:
        if "categories" in category.keys() and categoria in category["categories"]:
            return render_template("categoria.html",libros=datos,categoria=categoria)
    abort(404)

#Probar en el entorno virtual de desarrollo
app.run("0.0.0.0",5000,debug=True)