import streamlit as st
import requests
import json
import pandas as pd
import os

url = os.environ.get(
    "SENTIMENT_APP_URL", "https://afif2100-sentiment-app-lfww2ecnbq-et.a.run.app/"
)

st.title("Sentiment Analysis APP")


def check_api_status(url):
    try:
        response = requests.get(f"{url}/health", timeout=3)
        status = response.status_code
        st.success(f"API Status : {status}")
    except:
        st.exception("API is not Ready")


if st.button("Check API Status"):
    check_api_status(url)
else:
    check_api_status(url)


txt = st.text_area(
    "Text to analyze, seperate with comma",
    """Istilah ujaran kebencian cenderung dipahami sebagai segala jenis komunikasi berupa perkataan, tulisan maupun perilaku yang menyerang atau menggunakan bahasa merendahkan atau diskriminatif.""",
)

text = txt.split(",")
if not isinstance(text, list):
    text = [text]

if st.button("Check Sentiment of text"):
    payload = {"text": text}
    response = requests.post(f"{url}/api/v1/sentiment", data=payload)
    result = response.json()["result"]
    if len(text) == 1:
        rpd_ = pd.DataFrame([result])[["text", "label", "score"]]
    else:
        rpd_ = pd.DataFrame(result)[["text", "label", "score"]]
    st.write(rpd_)
