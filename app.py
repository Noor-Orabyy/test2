import streamlit as st
import joblib
import os

# LOAD MODELS SAFELY
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

url_model = joblib.load(os.path.join(BASE_DIR, "phishing_model.pkl"))
text_model = joblib.load(os.path.join(BASE_DIR, "text_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))

# FEATURE FUNCTION
def url_features(url):
    return [[
        len(url),
        url.count("."),
        url.count("-"),
        int("@" in url),
        int("https" in url)
    ]]

# UI
st.title("Phishing + Social Engineering Detector")

url = st.text_input("Enter URL")
msg = st.text_area("Enter message (optional)")

if st.button("Check"):

    result = "SAFE"

    # URL CHECK
    if url:
        pred = url_model.predict(url_features(url))[0]
        if pred == 1:
            result = "PHISHING"

    # TEXT CHECK
    if msg:
        x = vectorizer.transform([msg])
        pred2 = text_model.predict(x)[0]
        if pred2 == 1:
            result = "PHISHING"

    st.subheader("Result:")
    st.write(result)
