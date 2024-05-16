# My Movie DB

My Movie DB is a Flask-based web application that allows users to discover and explore movies and TV shows using the TMDB (The Movie Database) API. This application provides features such as browsing popular movies, top-rated movies, and searching for specific movies.

## Features

- Browse popular movies
- Explore top-rated movies
- Search for movies
- View detailed information about each movie, including cast, crew, trailers, and reviews

## Screenshots

![Home Page](static/images/homepage.png)
![Movie Details](static/images/moviedetails.png)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Vercel CLI (for deployment)

### Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/philh4420/movie-python.git
    cd mymoviedb
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your TMDB API key:**

    Replace `'your_tmdb_api_key_here'` with your actual TMDB API key in `config.py`.

5. **Run the application locally:**

    ```sh
    python main.py
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000
    ```

## Deployment

To deploy this application on Vercel, follow these steps:

1. **Install Vercel CLI:**

    ```sh
    npm install -g vercel
    ```

2. **Login to Vercel:**

    ```sh
    vercel login
    ```

3. **Deploy the application:**

    ```sh
    vercel
    ```

4. **Follow the prompts to complete the deployment.**

## Project Structure


