import joblib

model = joblib.load("social_model.pkl")      # adjust
vectorizer = joblib.load("vectorizer.pkl")   # adjust


def predict_text(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    print("DEBUG text prediction:", prediction)

    # ⚠️ adjust label mapping if needed
    if prediction == 1:
        return "phishing"
    else:
        return "safe"


if __name__ == "__main__":
    while True:
        text = input("Enter message: ")
        print("Result:", predict_text(text))
