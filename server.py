from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from musicDAO import musicDAO

app = Flask (__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/musics')
@cross_origin()
def getAll():
    results = musicDAO.getAll()
    return jsonify(results)


@app.route('/musics/<int:id>')
@cross_origin()
def findById(id):
    foundMusic = musicDAO.findByID(id)
    return jsonify(foundMusic)


@app.route('/musics', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)

    music = {
        "title": request.json['title'],
        "artist": request.json['artist'],
        "minutes": request.json['minutes'],
        "year": request.json['year'],
        "category": request.json['category'],
    }

    new_id = musicDAO.create(music)
    music['id'] = new_id
    return jsonify(music)


@app.route('/musics/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundMusic = musicDAO.findByID(id)
    if not foundMusic:
        abort(404)

    if not request.json:
        abort(400)

    reqJson = request.json

    if 'artist' in reqJson:
        foundMusic['artist'] = reqJson['artist']
    if 'title' in reqJson:
        foundMusic['title'] = reqJson['title']
    if 'minutes' in reqJson:
        foundMusic['minutes'] = reqJson['minutes']
    if 'year' in reqJson:
        foundMusic['year'] = reqJson['year']
    if 'category' in reqJson:
        foundMusic['category'] = reqJson['category']

    musicDAO.update(id, foundMusic)
    return jsonify(foundMusic)


@app.route('/musics/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    musicDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)

# END