from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from movieDAO import movieDAO

app = Flask (__name__, static_url_path='', static_folder='.')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/movies')
@cross_origin()
def getAll():
    results = movieDAO.getAll()
    return jsonify(results)


@app.route('/movies/<int:id>')
@cross_origin()
def findById(id):
    foundMovie = movieDAO.findByID(id)
    return jsonify(foundMovie)


@app.route('/movies', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)

    movie = {
        "title": request.json['title'],
        "minutes": request.json['minutes'],
        "year": request.json['year'],
        "category": request.json['category'],
    }

    new_id = movieDAO.create(movie)
    movie['id'] = new_id
    return jsonify(movie)


@app.route('/movies/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundMovie = movieDAO.findByID(id)
    if not foundMovie:
        abort(404)

    if not request.json:
        abort(400)

    reqJson = request.json

    if 'title' in reqJson:
        foundMovie['title'] = reqJson['title']
    if 'minutes' in reqJson:
        foundMovie['minutes'] = reqJson['minutes']
    if 'year' in reqJson:
        foundMovie['year'] = reqJson['year']
    if 'category' in reqJson:
        foundMovie['category'] = reqJson['category']

    movieDAO.update(id, foundMovie)
    return jsonify(foundMovie)


@app.route('/movies/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    movieDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)

# END