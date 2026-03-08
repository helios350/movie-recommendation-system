import pickle
import streamlit as st
import pandas as pd
import requests
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)

    vectors = pickle.load(open('vectors.pkl', 'rb'))

    return movies, vectors

movies, vectors = load_data()

def fetch_poster(movie_id):
    api_key = st.secrets["TMDB_API_KEY"]
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster+Found"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    target_vector = vectors[movie_index]
    similarity_scores = cosine_similarity(target_vector, vectors)[0]
    movies_list = sorted(list(enumerate(similarity_scores)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))
    
    return recommend_movies, recommend_movies_posters

st.title('Movie Recommendation System 🎥')

selected_movie_name = st.selectbox(
    "Select the movie:",
    movies['title'].values,
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.image(posters[i])
            st.text(names[i])