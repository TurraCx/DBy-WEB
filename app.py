from flask import Flask, render_template, request, jsonify
from modules import DanishBytes

app = Flask(__name__)
d = DanishBytes.DanishBytes()

@app.route("/")
def hello(name=None):
    return render_template('hello.html')

@app.route('/search', methods=['POST'])
def search():
    d.set_api(request.json['api_key'])
    return jsonify(d.find_movie(request.json['search'])['torrents'])

@app.route('/download', methods=['POST'])
def download():
    return jsonify(d.get_torrent(request.json['item']['id'])['attributes'])

@app.route('/magnet', methods=['POST'])
def magnet():
    tor = d.get_torrent(request.json['item']['id'])
    magnet = f"magnet:?dn={tor['attributes']['name']}&xt=urn:btih:{request.json['item']['info_hash']}&as={tor['attributes']['download_link']}&xl={tor['attributes']['size']}&tr=https://danishbytes.club/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes.org/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes2.org/announce/e064ba0c35d252338572fd7720448cc5&tr=https://danishbytes.art/announce/e064ba0c35d252338572fd7720448cc5"
    return magnet