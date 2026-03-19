from flask import Flask, render_template, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = "super_secret"
app.config["UPLOAD_FOLDER"] = "uploads"


@app.route('/')
def root():
    return redirect('/home')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/central')
def central():
    if 'usuario' not in session:
        return redirect('/home')
    return render_template('central.html')


@app.route('/logar', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']

    if usuario == 'lucas' and senha == '123':
        session['usuario'] = usuario
        return redirect('/central')

    return "Login inválido"
