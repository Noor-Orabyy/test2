import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("spam_msgs.csv")

texts = df["text"]
labels = df["label"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

joblib.dump(model, "text_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Text model saved")
