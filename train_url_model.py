import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# LOAD DATASET
df = pd.read_csv("phishing_site_urls.csv")

X_raw = df["URL"]
y = df["Label"]

# FEATURES
def extract_features(url):
    return [
        len(url),
        url.count("."),
        url.count("-"),
        int("@" in url),
        int("https" in url)
    ]

X = X_raw.apply(extract_features)
X = list(X)

# TRAIN
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")

print("URL MODEL SAVED ✔")
