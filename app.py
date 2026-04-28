import streamlit as st

st.markdown("""
<style>
.stApp {
    background-color: #e8f6ff;
    color: #1e3a5f;
}
</style>
""", unsafe_allow_html=True)


def load_malicious_db():
    try:
        with open("malicious_urls.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except:
        return []


def analyze_url(url, db):
    score = 0
    reasons = []

    if not url:
        return 0, ["No URL provided"], False

    if any(malicious in url for malicious in db):
        return 5, ["Matched malicious database entry"], True

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

    return score, reasons, False


def risk_level_url(score):
    if score >= 4:
        return "HIGH RISK"
    elif score >= 2:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


def back_button():
    if st.button("Back to Home"):
        st.session_state.page = "home"


def message_page():
    st.title("Message Analysis")

    q1 = st.checkbox("1. The message creates urgency (Act now, immediately)")
    q2 = st.checkbox("2. It asks for private information (password, credit card)")
    q3 = st.checkbox("3. It pretends to be a trusted company or person")
    q4 = st.checkbox("4. It asks you to click a link or login")
    q5 = st.checkbox("5. It offers something attractive (free, prize)")
    q6 = st.checkbox("6. It uses fear (virus detected, account blocked)")
    q7 = st.checkbox("7. It feels suspicious or unusual")
    q8 = st.checkbox("8. It pressures you not to think or verify")

    if st.button("Analyze Message"):

        score = 0
        reasons = []

        checks = [
            (q1, "Urgency detected"),
            (q2, "Requests private information"),
            (q3, "Impersonates trusted entity"),
            (q4, "Requests login or link click"),
            (q5, "Bait / reward offer"),
            (q6, "Fear-based manipulation"),
            (q7, "Suspicious behavior"),
            (q8, "Pressure without verification")
        ]

        for checked, reason in checks:
            if checked:
                score += 1
                reasons.append(reason)

        if score >= 6:
            level = "HIGH RISK"
        elif score >= 3:
            level = "MEDIUM RISK"
        else:
            level = "LOW RISK"

        st.subheader("Risk Level")
        st.write(level)

        st.write("Risk score (0-8) = " + str(score))

        st.subheader("Reasons")
        for r in reasons:
            st.write(r)

    back_button()


def url_page():
    st.title("Link Analysis")

    db = load_malicious_db()

    url = st.text_input("Enter URL")

    if st.button("Analyze Link"):

        score, reasons, matched = analyze_url(url, db)

        if matched:
            level = "HIGH RISK (DATABASE MATCH)"
        else:
            level = risk_level_url(score)

        st.subheader("Risk Level")
        st.write(level)

        st.write("Risk score (0-5) = " + str(score))

        st.subheader("Reasons")
        for r in reasons:
            st.write(r)

    back_button()


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


if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "url":
    url_page()
elif st.session_state.page == "msg":
    message_page()
