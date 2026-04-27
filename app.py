import streamlit as st

# -----------------------------
# BACKGROUND COLOR (CSS)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #e8f6ff;
    color: #1e3a5f;
}
</style>
""", unsafe_allow_html=True)


# -----------------------------
# FUNCTIONS
# -----------------------------
def url_page():
    st.title("🔗 Check Link")

    url = st.text_input("Enter URL")

    if st.button("Analyze Link"):
        score = 0

        if url:
            if len(url) > 75:
                score += 1
            if "@" in url:
                score += 1
            if url.count("-") > 3:
                score += 1
            if url.count(".") > 4:
                score += 1
            if "https" not in url:
                score += 1

        if score >= 2:
            st.error("🚨 PHISHING LINK")
        else:
            st.success("✅ SAFE LINK")


def message_page():
    st.title("💬 Check Message")

    st.write("Select suspicious indicators:")

    choices = st.text_input("Enter numbers (e.g. 1,3,5)")

    if st.button("Analyze Message"):
        score = 0

        if choices:
            selected = choices.split(",")
            score = len(selected)

        if score >= 5:
            st.error("🚨 HIGH RISK")
        elif score >= 3:
            st.warning("⚠️ MEDIUM RISK")
        else:
            st.success("✅ LOW RISK")


# -----------------------------
# HOME PAGE
# -----------------------------
st.title("🛡️ Security Detector System")

st.write("Choose an option:")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔗 Check Link"):
        st.session_state.page = "url"

with col2:
    if st.button("💬 Check Message"):
        st.session_state.page = "msg"


# -----------------------------
# PAGE ROUTING
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "url":
    url_page()

elif st.session_state.page == "msg":
    message_page()

else:
    st.write("Welcome 👋 Select a feature above")
