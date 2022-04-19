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