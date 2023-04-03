from flask import Flask, jsonify
import requests
movie_url = "https://swapi.dev/api/films/"

def list_movies_controller():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    return jsonify(data["results"])

def sort_movies():
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "name": movie["title"]} for movie in data["results"]]
    movies.sort(key=lambda x: x["id"])
    return jsonify(movies)

def get_characters(id):
    data = requests.get(movie_url).json()
    movies = [{"id": movie["episode_id"], "characters": movie["characters"]} for movie in data["results"]]
    movies.sort(key=lambda x: x["id"])
    results = movies[int(id)-1]["characters"]
    character_names = []
    for character in results:
        name = requests.get(character).json()
        character_names.append(name["name"])
    return jsonify(character_names)