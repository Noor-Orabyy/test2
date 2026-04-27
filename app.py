import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #e8f6ff;
    color: #1e3a5f;
}
</style>
""", unsafe_allow_html=True)


def analyze_url(url):
    score = 0
    reasons = []

    if not url:
        return 0, ["No URL provided"]

    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    if "@" in url:
        score += 1
        reasons.append("Contains '@' symbol")

    if url.count("-") > 3:
        score += 1
        reasons.append("Excessive hyphens")

    if url.count(".") > 4:
        score += 1
        reasons.append("Multiple subdomains")

    if "https" not in url:
        score += 1
        reasons.append("Not using HTTPS")

    return score, reasons


def risk_level(score):
    if score >= 4:
        return "HIGH RISK"
    elif score >= 2:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def home_page():
    st.title("Security Detector System")

    st.subheader("Guidelines for Online Safety Awareness")

    st.write("""
This is not an official method for identifying attacks, so always exercise caution.

Never click on a link without verifying it first. You can hover your cursor over it to see the actual destination.

Report any social engineering attacks to your local authorities.

Regularly educate users about online safety, emphasizing the importance of avoiding suspicious links and not sharing personal information.

Stay informed and help educate those around you about the dangers of social engineering.
""")

    col1, col2 = st.columns(2)

    if col1.button("Check Link"):
        st.session_state.page = "url"

    if col2.button("Check Message"):
        st.session_state.page = "msg"


def url_page():
    st.title("Link Analysis")

    url = st.text_input("Enter URL")

    if st.button("Analyze"):
        score, reasons = analyze_url(url)
        level = risk_level(score)

        st.subheader("Risk Level")
        st.write(level)

        st.subheader("Risk Score (0-5)")
        st.write(score)

        st.subheader("Reasons")
        for r in reasons:
            st.write(r)


def message_page():
    st.title("Message Analysis")

    text = st.text_area("Enter message")

    if st.button("Analyze"):
        score = 0
        reasons = []

        keywords = {
            "password": "Requests credentials",
            "urgent": "Creates urgency",
            "bank": "Financial impersonation",
            "click": "Suspicious link encouragement",
            "verify": "Identity verification scam"
        }

        if text:
            for k, v in keywords.items():
                if k in text.lower():
                    score += 1
                    reasons.append(v)

        level = risk_level(score)

        st.subheader("Risk Level")
        st.write(level)

        st.subheader("Risk Score (0-5)")
        st.write(score)

        st.subheader("Reasons")
        for r in reasons:
            st.write(r)


if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "url":
    url_page()
elif st.session_state.page == "msg":
    message_page()
