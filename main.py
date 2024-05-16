from flask import Flask, render_template, request
import requests
from config import API_KEY

app = Flask(__name__)


@app.route("/")
def index():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
    response = requests.get(url)
    movies = (
        response.json()["results"][:5] if response.status_code == 200 else []
    )  # Fetch top 5 popular movies
    return render_template("index.html", title="Home", movies=movies)


@app.route("/popular")
def popular_movies():
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
    response = requests.get(url)
    movies = response.json()["results"] if response.status_code == 200 else []
    return render_template("popular.html", movies=movies, title="Popular Movies")


@app.route("/top_rated")
def top_rated_movies():
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}"
    response = requests.get(url)
    movies = response.json()["results"] if response.status_code == 200 else []
    return render_template("top_rated.html", movies=movies, title="Top Rated Movies")


@app.route("/movie/<int:movie_id>")
def movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=credits,videos,images,reviews,similar"
    response = requests.get(url)
    movie = response.json() if response.status_code == 200 else {}
    return render_template("movie_details.html", movie=movie)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    if query:
        url = (
            f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}"
        )
        response = requests.get(url)
        movies = response.json()["results"] if response.status_code == 200 else []
        return render_template(
            "search_results.html", movies=movies, title="Search Results"
        )
    return render_template("search.html", title="Search Movies")


if __name__ == "__main__":
    app.run(debug=True)
