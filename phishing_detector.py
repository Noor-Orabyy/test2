import numpy as np
import joblib
from urllib.parse import urlparse

# =========================
# LOAD MODEL
# =========================
model = joblib.load("phishing_model.pkl")  # adjust if needed


# =========================
# NORMALIZE URL
# =========================
def normalize_url(url):
    if not url.startswith("http"):
        url = "http://" + url
    return url


# =========================
# FEATURE EXTRACTION
# =========================
def extract_features(url):
    parsed = urlparse(url)

    features = []

    # URL length
    features.append(len(url))

    # count dots
    features.append(url.count('.'))

    # has @
    features.append(1 if '@' in url else 0)

    # has hyphen in domain
    features.append(1 if '-' in parsed.netloc else 0)

    # number of subdomains
    features.append(len(parsed.netloc.split('.')) - 2)

    # https
    features.append(1 if parsed.scheme == "https" else 0)

    return np.array(features).reshape(1, -1)


# =========================
# PREDICT
# =========================
def predict_url(url):
    url = normalize_url(url)
    features = extract_features(url)

    prediction = model.predict(features)[0]
    prob = model.predict_proba(features)[0]

    print("DEBUG URL:", url)
    print("DEBUG prediction:", prediction)
    print("DEBUG prob:", prob)

    # ⚠️ IMPORTANT: adjust this if needed
    # ASSUMING: 1 = phishing
    if prediction == 1:
        return "phishing"
    else:
        return "safe"


# =========================
# TEST
# =========================
if __name__ == "__main__":
    while True:
        url = input("Enter URL: ")
        print("Result:", predict_url(url))
