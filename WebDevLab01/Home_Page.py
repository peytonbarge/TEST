import streamlit as st
#import info
import pandas as pd
# about ME
import datetime

st.write("Peyton Barge, CS 1301")
st.markdown(
    """
    <style>
    .stApp {
        background-color: pink;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Home Page</h1>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h1 style='text-align: center; color: white; font-family: Pacifico;'>My Website</h1>
    """,
    unsafe_allow_html=True
)
st.write("Welcome to my interactive website, a fun and personalized reflection of who I am. Since this lab was all about me, I took the opportunity to infuse it with as much of my personality as possible. From the vibrant pink background to the playful tone and layout, every section was designed to feel authentically me. I really enjoyed this assignment, especially the creative freedom it allowed. I used a number of different functions throughout. In my phase II tab I have 3 interactive functions. The first one is a mood tracker where you can rate your mood and see the trend. Secondly I have an interactive timeline, considering the site is about me i thought this was relevant. Last I have an interactive plot line of would you rather questions to better know the user. All interactive graphs required streamlit and pandas to be imported, the mood tracker included those two as well as datetime to be imported. Being able to customize and build on the original template made this one of the most enjoyable and expressive parts of CS 1301. ")

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

image_path = "images/homepage.jpg"


st.image(image_path, caption="My favorite moments", use_container_width=True)

st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
