from flask import Flask, jsonify, request
from cortes_de_carne import cortes_de_carne

app = Flask(__name__)


@app.route("/cortes", methods=["GET"])
def get_cortes():
    return jsonify({"cortes_de_carne": cortes_de_carne})


@app.route("/test", methods=["POST"])
def set_test():
    data = request.get_json()

    res = {"message": "aqui", "data": data}
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=True)
