import streamlit as st
import joblib

# load models
url_model = joblib.load("phishing_model.pkl")
text_model = joblib.load("text_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def url_features(url):
    return [[
        len(url),
        url.count("."),
        url.count("-"),
        int("@" in url),
        int("https" in url)
    ]]


st.title("Phishing & Social Engineering Detector")

# INPUT
url = st.text_input("Enter URL")
msg = st.text_area("Enter message (optional)")

# PREDICT
if st.button("Check"):

    result = "SAFE"

    # URL prediction
    if url:
        pred = url_model.predict(url_features(url))[0]
        if pred == 1:
            result = "PHISHING"

    # text prediction
    if msg:
        x = vectorizer.transform([msg])
        pred2 = text_model.predict(x)[0]
        if pred2 == 1:
            result = "PHISHING"

    st.subheader("Result:")
    st.write(result)
