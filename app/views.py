
from flask import render_template
from app import app
from .request import get_movies,get_movie

# views
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
  '''
  View movie page function that returns the movie details page and its data
  '''
  message = 'Hello World'
  return render_template('movie.html',id = movie_id)
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

# Getting popular movie(Making the API call)
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to the best Movie Website Review Website Online'
    return render_template('index.html',title = title,popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
