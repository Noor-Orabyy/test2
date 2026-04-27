from phishing_detector import predict_url
from social_eng_det import predict_text
from decision_logic import final_decision


def main():
    while True:
        print("\n--- Phishing Detection System ---")

        url = input("Enter URL: ")
        text = input("Enter message (optional): ")

        phishing_result = predict_url(url)
        social_result = predict_text(text) if text.strip() != "" else "safe"

        final_result = final_decision(phishing_result, social_result)

        print("\nFINAL RESULT:", final_result)


if __name__ == "__main__":
    main()
