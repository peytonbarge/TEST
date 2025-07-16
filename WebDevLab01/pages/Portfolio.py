
import streamlit as st
#import info
import pandas as pd
# about ME
import datetime

#.streamlit/config.toml
# More accurate Streamlit background override
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
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>PB</h1>
    """,
    unsafe_allow_html=True
)
st.write("How did I end up here?")
def about_me_section():
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Dancing Script;'>About Me</h1>
    """,
    unsafe_allow_html=True
)
    #st.image("images/IMG_5696.jpeg", width = 700)
    st.write("I'm Peyton Barge. I am an incoming freshman student at Georgia Tech from Atlanta. ")
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

about_me_section()


# links - Sidebar

def links_section():
    st.markdown(
    
    """
    <style>
    [data-testid="stSidebar"] {
        background-image: url("https://www.bing.com/th/id/OGC.a59006794e8d64a381e0f78162f202b0?o=7&pid=1.7&rm=3&rurl=https%3a%2f%2fcur.glitter-graphics.net%2fpub%2f3703%2f3703891tuiwgbkg7n.gif&ehk=5YAMQ7JSB9QxZHZr74L0ucRdnXTavcj6hEyqLl7Xyqw%3d");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.sidebar.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Lets Be Friends!</h1>
    """,
    unsafe_allow_html=True
)
    st.sidebar.text("Connect with me on LinkdIn")
    linkedin_link = f'<a href = "http://www.linkedin.com/in/peyton-barge-3a66a4374"><img src = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg" alt = "LinkedIn" width = "75" height = "75" ></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html = True)
    st.sidebar.text("Follow Me on Instagram!")
    github_link = f'<a href ="https://www.instagram.com/pbarge323?igsh=YjF5c3NxczhkYXJh&utm_source=qr"><img src="https://th.bing.com/th/id/ODF.Tw-tjGfaKLIkitkJNlB7SA?w=32&h=32&qlt=90&pcl=fffffc&o=6&pid=1.2" alt = "Github" width = "65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html = True)
    st.sidebar.text("Or email me!")
    email_html = '<a href="mailto:pbarge3@gatech.edu"><img src="https://logowik.com/content/uploads/images/513_email.jpg" alt="Email" width="75" height="75"></a>'

    st.sidebar.markdown(email_html, unsafe_allow_html=True)


links_section()


# Education
# ** make the text bold
def education_section(education_data, course_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>The Beginning</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader(f"**{education_data['name']}**")
    st.write(f"**Born:**{education_data['Born']}")
    st.write(f"**Location:**{education_data['Location']}")
    st.write(f"**Siblings and Pets:**{education_data['Siblings and Pets']}")
    st.write("**SCHOOL LIFE**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "elem":"Elementary",
        "middle":"Middle",
        "High":"High School",
        "college":"College"},
        hide_index=True,        
        )
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
education_section({
    'Born': 'May 10, 2007 (age 18 years)',
    'name': 'Peyton Kea Barge',
    'Location': 'Atlanta, GA',
    'Siblings and Pets': 'Abby, J, Ethel, Lucy(m. 2000 - 2014)',
    'GPA': '4.0'
},  {
    "elem":["E. Rivers Elementary", "Located in Atlanta, GA", "Grades K-5"], 
    "middle":["Sutton Middle School", "Located in Atlanta, GA", "Grades 6-7"], 
    "High":["Rabun Gap Nacoochee School", "Located in Dillard, GA", "Grades 8-12"],
    "college":["Georgia Tech", "Located in Atlanta, GA", "4 year institution"],
    })

#Professional Experience
def experience_section(experience_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Hobbies and Jobs</h1>
    """,
    unsafe_allow_html=True
)
    for job_title,(job_description) in experience_data.items():
        expander= st.expander(f"{job_title}")
        #expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)

        st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')

experience_section({
    "JOBS": (
        ["THE SHAK", "- Worked in an Ice Cream shop on the lake",
         "- Responsible for training trainees", "- Responsible for keeping up with profit"],
        #"images/IMG_0350.jpg"
    ),
    "HI-UP at Rockbrook Camp for Girls": (
        ["HI-UP", "- Leadership role at a sleep away camp in Brevard, NC",
         "- Tasked with setting and scraping meals as well as babysitting younger campers"],
        #"images/IMG_4567.jpg"
    ),
    "Piano": (
        ["- 7 years of piano, it is my favorite pass time"],
        #"images/IMG_9002.jpeg"
    )
})


# Project Section
def project_section(projects_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>Skills</h1>
    """,
    unsafe_allow_html=True
)
    projects_data = {
    "Expert Napper": "Could nap multiple times a day, favorite time is 3pm-5pm",
}
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
project_section({
    "Expert Napper": "Could nap multiple times a day, favorite time is 3pm-5pm",
})

#Skills

spoken_icons = {"French": "🇫🇷",
    "English": "🇬🇧",
    "Spanish":"🇪🇸"
}

def skills_section(programming_data, spoken_data):
    st.markdown(
    """
    <h1 style='text-align: center; color: hotpink; font-family: Pacifico;'>My Hot Takes</h1>
    """,
    unsafe_allow_html=True
)
    st.subheader("Agree or am I crazy?")
    programming_icons = {
    "Pineapple belongs on pizza": "🍕",
    "Socks shouldn't have to match": "🧦",
    "Birds aren't real": "🐦",
}
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Fun Facts")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{spoken_icons.get(spoken,'')}: {proficiency}")

    st.write('🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸')
spoken_data = {
    "1": "There are 5 Peytons before me (they are all boys)",
    "2": "I am fluent in Spanish",
    "3": "I am a quarter Vietnamese",}

programming_data = {
    "Pineapple belongs on pizza": 95,
    "Socks shouldn't have to match": 70,
    "Birds aren't real": 40,
}
skills_section(programming_data, spoken_data)


