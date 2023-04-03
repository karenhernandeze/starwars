import os
from flask import Flask, jsonify
from .controller import list_movies_controller, sort_movies, get_characters

print("Application startup")
# port = 3000
port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"

@app.route("/", methods=['GET'])
def list_movies():
    movies = list_movies_controller()
    return movies

@app.route("/sorted", methods=['GET'])
def list_movies_sorted():
    movies = sort_movies()
    return movies

@app.route("/<id>", methods=['GET'])
def list_movies_characters(id):
    character_names = get_characters(id)
    return character_names

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=port)
