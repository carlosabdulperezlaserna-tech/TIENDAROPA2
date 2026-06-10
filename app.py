from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Tienda de Ropa</h1>
    <p>Bienvenido a nuestra tienda.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)