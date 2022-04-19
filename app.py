from flask import Flask, render_template, abort
import json
import os
app = Flask (__name__)

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for book in datos:
        if "isbn" in book.keys() and isbn == book["isbn"]:
            return render_template("libro.html",libro=book)
    abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    for cat in datos:
        if "categories" in cat.keys() and categoria in cat["categories"]:
            return render_template("categoria.html",libros=datos,categoria=categoria)
    abort(404)