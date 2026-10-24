
from pathlib import Path

from flask import Flask, jsonify
import functions as f


application = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
data = f.load_file(str(BASE_DIR / "heroes.csv"))


@application.route("/", methods=["GET"])
def index():
    """Retorna todos los héroes registrados."""
    return jsonify(data), 200


@application.route("/<string:id_heroe>", methods=["GET"])
def heroe(id_heroe):
    """Retorna un héroe por su identificador."""

    if id_heroe not in data:
        return jsonify({"error": "Héroe no encontrado"}), 404

    return jsonify(data[id_heroe]), 200


if __name__ == "__main__":
    application.run(port=5000, debug=True)
