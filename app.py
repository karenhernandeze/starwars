import os
from flask import Flask, jsonify
import requests
import asyncio

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
    character_names = []
    for character in results:
        name = requests.get(character).json()
        character_names.append(name["name"])
        # print(name)
    # movie_id = request.args.get('id', default=1)
    # response = requests.get(f'{movie_url}{movie_id}').json()
    # character_urls = response['characters']
    # character_list = asyncio.run(get_all_movie_character_names(character_urls))
    # return jsonify({ 'movie_id': movie_id, 'title': response['title'], 'characters': character_list })

    return jsonify(character_names)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=port)
