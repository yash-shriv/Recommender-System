# We can use Flask for website development, But here I use Streamlit library to make it easy.
# Optional: Also try to build website with Flask or Django and add the ML model to it.

import streamlit as st
import pickle
import pandas as pd
import requests

# This function takes a movie id and hits the api. we need to import request lib to hit(request) api


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    # convert response to json
    data = response.json()

    return "https://image.tmdb.org/t/p/w780/asmCFd6BnqPkwIj0jHzcJXgNJvi.jpg" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_names = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API, time 01:50:00
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_posters

# I have convert dataframe to dictionary


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values)

# Add button (Take reference from streamlit documentation for creating/doing anything on website.)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col3:
        st.text(names[3])
        st.image(posters[3])
    with col3:
        st.text(names[4])
        st.image(posters[4])
