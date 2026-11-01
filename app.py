import streamlit as st
import re

st.title("🛡️ PhishGuard")

st.write("Check a URL for suspicious characteristics.")

url = st.text_input("Enter a URL")

if url:
    score = 0
    reasons = []

    # Check suspicious keywords
    suspicious_words = [
        "login",
        "verify",
        "account",
        "password",
        "secure",
        "update"
    ]

    for word in suspicious_words:
        if word.lower() in url.lower():
            score += 1
            reasons.append(f"Contains suspicious keyword: {word}")

    # Check for IP address
    ip_pattern = r"https?://\d{1,3}(\.\d{1,3}){3}"

    if re.match(ip_pattern, url):
        score += 2
        reasons.append("Uses an IP address instead of a domain name")

    # Check for @ symbol
    if "@" in url:
        score += 2
        reasons.append("Contains an @ symbol")

    # Check URL length
    if len(url) > 100:
        score += 1
        reasons.append("URL is unusually long")

    # Check HTTPS
    if not url.lower().startswith("https://"):
        score += 1
        reasons.append("Does not use HTTPS")

    # Result
    st.subheader("Analysis")

    st.write("Risk score:", score)

    if score == 0:
        st.success("✅ Low risk based on these checks.")

    elif score <= 2:
        st.warning("⚠️ Some suspicious characteristics detected.")

    else:
        st.error("🚨 High risk characteristics detected.")

    if reasons:
        st.write("Reasons:")
        for reason in reasons:
            st.write("•", reason)