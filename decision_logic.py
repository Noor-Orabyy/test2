def final_decision(phishing_result, social_result):
    print("DEBUG phishing:", phishing_result)
    print("DEBUG social:", social_result)

    # ✅ ANY detector flags → phishing
    if phishing_result == "phishing" or social_result == "phishing":
        return "phishing"
    else:
        return "safe"
