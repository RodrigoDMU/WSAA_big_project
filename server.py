# -----------------------------------------------------------------------------------------------------
# Server for Music Management
# -----------------------------------------------------------------------------------------------------
# Author: Rodrigo De Martino Ucedo
# -----------------------------------------------------------------------------------------------------

# Import libraries.
from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from musicDAO import musicDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app) # Allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# Route to get all music records.
@app.route('/musics')
@cross_origin()
def getAll():
    results = musicDAO.getAll() # Retrieve all music from DAO.
    return jsonify(results) # Return as JSON response.

# Route to get a single music record by its ID.
@app.route('/musics/<int:id>')
@cross_origin()
def findById(id):
    foundMusic = musicDAO.findByID(id) # Find music by ID.
    return jsonify(foundMusic) # Return the found music as JSON.

# Route to create a new music record (POST).
@app.route('/musics', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400) # Bad request if no JSON sent.

        # Build a music dictionary from request JSON data.
    music = {
        "artist": request.json['artist'],
        "title": request.json['title'],
        "minutes": request.json['minutes'],
        "year": request.json['year'],
        "category": request.json['category'],
    }
 
    # Create new music entry in DAO and get the new object (with ID).
    new_music = musicDAO.create(music)
    return jsonify(new_music) # Return the created music as JSON.

# Route to update an existing music record by ID (PUT).
@app.route('/musics/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundMusic = musicDAO.findByID(id) # Find the music to update.
    if not foundMusic:
        abort(404) # Not found if ID does not exist.

    if not request.json:
        abort(400) # Bad request if no JSON sent.

    reqJson = request.json
   
    # Update fields if present in JSON request.
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

    musicDAO.update(id, foundMusic) # Persist the updated music in DAO.
    return jsonify(foundMusic) # Return the updated music as JSON.

# Route to delete a music record by ID (DELETE).
@app.route('/musics/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    musicDAO.delete(id) # Delete the music by ID in DAO.
    return jsonify({"done": True}) # Return confirmation JSON.


if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app in debug mode.

# END.