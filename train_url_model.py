import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# load dataset
df = pd.read_csv("phishing_site_urls.csv")

# IMPORTANT: adjust if your dataset columns differ
X = df["URL"]
y = df["Label"]

# simple feature engineering (basic version)
def extract_features(url):
    return [
        len(url),
        url.count("."),
        url.count("-"),
        int("@" in url),
        int("https" in url)
    ]

X = X.apply(extract_features)
X = list(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "phishing_model.pkl")

print("URL model saved")
