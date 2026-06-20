from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def reloj():
    hora = datetime.now().strftime("%H:%M:%S")
    return f"""
    <html>
    <head>
        <title>Reloj Flask Estudiante A</title>
    </head>
    <body style="font-family:Arial;text-align:center;margin-top:100px;">
        <h1>Reloj Digital</h1>
        <h2>{hora}</h2>
        <p>Aplicación Flask para DevOps</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)