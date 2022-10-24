import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write(
    """
# Hafizhan Aliady, S.Stat,
##### *Resume* 
"""
)

image = Image.open("images/dp.jpg")
st.image(image, width=150)

st.markdown("## Summary", unsafe_allow_html=True)
st.info(
    """
Hello, I'm Hafizhan Aliady, I am a person who works on data, or what we usually call Data Science. 
I am a person who has a Speciality in Machine Learning engineering and MLOps \n
Have experience in building machine learning platforms to support data scientists deploying their model/products to become something that can make an impact.
I'm happy to help the data science team to increase their productivity through machine learning engineering.
"""
)

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True,
)

st.markdown(
    """
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://youtube.com/dataprofessor" target="_blank">Hafizhan Aliady</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bioinformatics-tools">Tools</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""",
    unsafe_allow_html=True,
)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f"`{a}`")
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.markdown(
    """
## Education
"""
)

txt(
    "**Bachelor of Statistics** (Data Science), *Universitas Islam Indonesia*, D.I Yogyakarta, Indonesia",
"")
st.markdown(
    """
- GPA: `3.64`
- Thesis awarded `1st` Prize by the National Research Council of Thailand.
"""
)


#####################
st.markdown(
    """
## Work Experience
"""
)

txt(
    "**Head, Center of Data Mining and Biomedical Informatics**, Faculty of Medical Technology, Mahidol University, Thailand",
    "2011-2021",
)
st.markdown(
    """
- Managing a Center of `10` professors, researchers and students to ensure KPIs are strategically achieved namely to publish at least `20+` research publications annually. 
- Actively took part in the talent hiring process as well as help employees to plan and develop their career path.
- Set budget and handle procurement in order to facilitate education and research activities. Secured `> 10 million THB` budget.
- Set and reflect on OKR on an annual basis to ensure productivity strategically matches the organization's direction.
"""
)

txt(
    "**Associate Professor**, Faculty of Medical Technology, Mahidol University, Thailand",
    "2012-2021",
)
txt(
    "**Assistant Professor**, Faculty of Medical Technology, Mahidol University, Thailand",
    "2009-2012",
)
txt(
    "**Lecturer**, Faculty of Medical Technology, Mahidol University, Thailand",
    "2006-2009",
)

#####################
st.markdown(
    """
## Bioinformatics Tools
"""
)
txt4(
    "ABCpred",
    "A web server for the discovery of acetyl- and butyryl-cholinesterase inhibitors",
    "http://codes.bio/abcpred/",
)
txt4(
    "AutoWeka",
    "An automated data mining software based on Weka",
    "http://www.mt.mahidol.ac.th/autoweka/",
)

#####################
st.markdown(
    """
## Skills
"""
)
txt3("Programming", "`Python`, `R`, `Linux`")
txt3("Data processing/wrangling", "`SQL`, `pandas`, `numpy`")
txt3("Data visualization", "`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`")
txt3("Machine Learning", "`scikit-learn`")
txt3("Deep Learning", "`TensorFlow`")
txt3("Web development", "`Flask`, `HTML`, `CSS`")
txt3(
    "Model deployment",
    "`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`",
)

#####################
st.markdown(
    """
## Social Media
"""
)
txt2("LinkedIn", "https://www.linkedin.com/in/hafizhan-aliady")
txt2("GitHub", "https://github.com/afif2100/")
