from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# Crear base de datos
def crear_bd():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        password TEXT
    )
    """)

    conexion.commit()
    conexion.close()


# Guardar usuario
def registrar_usuario(usuario, password):

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO usuarios(usuario,password) VALUES (?,?)",
        (usuario,password_hash)
    )

    conexion.commit()
    conexion.close()


# Validar usuario
def validar(usuario,password):

    password_hash = hashlib.sha256(
        password.encode()
    ).hexdigest()

    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario=? AND password=?",
        (usuario,password_hash)
    )

    resultado = cursor.fetchone()

    conexion.close()

    return resultado


@app.route("/")
def inicio():

    return """
    <h1>Login DRY7122</h1>

    <form action="/login" method="post">

    Usuario:
    <input name="usuario">

    <br>

    Contraseña:
    <input type="password" name="password">

    <br>

    <button>
    Ingresar
    </button>

    </form>
    """


@app.route("/login", methods=["POST"])
def login():

    usuario=request.form["usuario"]
    password=request.form["password"]


    if validar(usuario,password):

        return "Usuario validado correctamente"

    else:

        return "Usuario o contraseña incorrecta"


crear_bd()


# Usuarios integrantes
registrar_usuario("max", "1234")
registrar_usuario("matias", "1234")


app.run(host="0.0.0.0", port=5800)
