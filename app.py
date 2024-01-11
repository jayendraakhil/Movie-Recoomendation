import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_lottie import st_lottie



st.title('MOVIE RECOMMENDATION SYSTEM')


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_url_download = "https://lottie.host/920d732f-6805-437c-970c-383b4a57ead1/TMzLe4CE1F.json"
lottie_hello = load_lottieurl(lottie_url_download)
st_lottie(lottie_hello, key="hello",height=400,width=400)


def fetch_poster(movie_id):
    response =requests.get( "https://api.themoviedb.org/3/movie/{}?api_key=e3d62b9a13897076e368a85afc2cb5d5&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def rec(movie):
    mov_i=movies[movies['title']== movie].index[0]
    dis=similarity[mov_i]
    mov_lis=sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in mov_lis:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


movies_dict=pickle.load(open('m_dct.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
option=st.selectbox('Choose a Movie?',movies['title'].values)
if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters = rec(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
