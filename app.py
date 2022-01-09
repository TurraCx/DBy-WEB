from flask import Flask, render_template, request, jsonify
from modules import DanishBytes

app = Flask(__name__)
d = DanishBytes.DanishBytes()

@app.route("/")
def hello(name=None):
    return render_template('hello.html')

@app.route('/mirrors', methods=['GET'])
def mirrors():
    return jsonify(d.check_mirrors())

@app.route('/search', methods=['POST'])
def search():
    d.set_api(request.json['api_key'])
    return jsonify(d.find_movie(request.json['search']))

if __name__ == "__main__":
    app.run(port=3000)