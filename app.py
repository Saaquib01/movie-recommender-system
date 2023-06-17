import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

option = st.selectbox('Which Movie recommendation would you like to have?', movies['title'].values)

if st.button('Recommend'):
    recommemdations = recommend(option)
    for i in recommemdations:
        st.write(i)