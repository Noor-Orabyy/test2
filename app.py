import streamlit as st

# -----------------------------
# SOCIAL ENGINEERING TACTICS
# -----------------------------
TACTICS = {
    "1": "Urgency - Creates pressure to act quickly",
    "2": "Private Info Request - Asks for sensitive data",
    "3": "Phishing - Fake trusted brand messages",
    "4": "Pretexting - Fake identity/scenario",
    "5": "Baiting - Offers something tempting",
    "6": "Scareware - Fake warning threats",
    "7": "Honey Trap - Emotional manipulation",
    "8": "Quid Pro Quo - Exchange of service for info"
}

# -----------------------------
# URL CHECK (simple heuristic)
# -----------------------------
def url_check(url):
    if not url:
        return "SAFE"

    score = 0

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

    return "PHISHING" if score >= 2 else "SAFE"


# -----------------------------
# MESSAGE CHECK (tactic-based)
# -----------------------------
def message_check(choices):
    score = 0

    selected = choices.split(",")

    for c in selected:
        c = c.strip()
        if c in TACTICS:
            score += 1

    if score >= 5:
        return "HIGH RISK"
    elif score >= 3:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.title("Phishing & Social Engineering Detector")

st.subheader("Enter URL")
url = st.text_input("URL")

st.subheader("Select Social Engineering Tactics")

for k, v in TACTICS.items():
    st.write(f"{k}. {v}")

choices = st.text_input("Enter numbers (comma separated like 1,3,5)")

# -----------------------------
# RUN DETECTION
# -----------------------------
if st.button("Check"):

    url_result = url_check(url)
    msg_result = message_check(choices)

    # FINAL DECISION LOGIC
    if url_result == "PHISHING" or msg_result in ["HIGH RISK", "MEDIUM RISK"]:
        final = "🚨 RISK DETECTED"
    else:
        final = "✅ SAFE"

    st.subheader("RESULT")
    st.write(final)

    st.write("URL Status:", url_result)
    st.write("Message Risk:", msg_result)
