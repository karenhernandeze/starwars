import os
from flask import Flask, jsonify
import requests

print("Application startup")
port = 3000
# port = int(os.environ['PORT'])
print("PORT::", port)

app = Flask(__name__)

movie_url = "https://swapi.dev/api/films/"

@app.route("/", methods=['GET'])
def list_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return jsonify(data["results"])

@app.route("/sorted", methods=['GET'])
def list_movies_sorted():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    movies.sort(key=lambda x: x["id"])
    return jsonify(movies)

@app.route("/<id>", methods=['GET'])
def list_movies_characters(id):
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "characters": movie["characters"]} for movie in data["results"]]
    movies.sort(key=lambda x: x["id"])
    results = movies[int(id)-1]["characters"]
    return jsonify(results)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=port)
