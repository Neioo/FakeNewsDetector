# fake_news_app.py
import streamlit as st
import joblib

nb_model = joblib.load("lr_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Placeholder for your ML model
# You will load your trained model here later
# For now, simulate prediction for demonstration
# def predict_fake_news(title, text):
#     combined_text = f"{title.strip()} {text.strip()}"
#     if len(combined_text) < 10:
#         return "Please enter a longer headline and news text."

#     # Vectorize the combined input
#     text_vector = vectorizer.transform([combined_text])

#     # Predict using the loaded model
#     prediction = svm_model.predict(text_vector)[0]
    
#     return "⚠️ FAKE NEWS" if prediction == 0 else "✅ REAL NEWS"

def predict_fake_news(title, text):
    combined_text = f"{title.strip()} {text.strip()}"
    if len(combined_text) < 10:
        return "Please enter a longer headline and news text.", None
    
    vector = vectorizer.transform([combined_text])
    prediction = nb_model.predict(vector)[0]
    confidence = nb_model.predict_proba(vector)[0][prediction]

    label = "⚠️ FAKE NEWS" if prediction == 0 else "✅ REAL NEWS"
    return label, confidence


# Streamlit app
st.set_page_config(page_title="Fake News Detector", layout="centered")

st.title("📰 Fake News Detection Web App")
st.markdown("Paste a news headline and short paragraph to see if it's fake or real.")

# User input
title_input = st.text_input('Enter news headline here')
user_input = st.text_area("Enter news text here", height=150)

# Predict button
# if st.button("Check News"):
#     if title_input.strip() == "" or user_input.strip() == "":
#         st.warning("Please enter both a headline and news text.")
#     else:
#         prediction = predict_fake_news(title_input, user_input)
#         st.subheader("🔎 Prediction Result:")
#         st.success(prediction)

if st.button("Check News"):
    if title_input.strip() == "" or user_input.strip() == "":
        st.warning("Please enter both a headline and news text.")
    else:
        label, confidence = predict_fake_news(title_input, user_input)
        st.subheader("🔎 Prediction Result:")

        if "FAKE" in label:
            st.warning(f"{label} — Confidence: {confidence * 100:.2f}%")
        else:
            st.success(f"{label} — Confidence: {confidence * 100:.2f}%")

        st.progress(int(confidence * 100))

        
st.markdown("""
    ---
    📝 **Disclaimer**:  
    The prediction is generated by an AI model and may not always reflect the truth.  
    Confidence levels below 70% indicate uncertainty — please verify the information using trusted news sources.
    """, unsafe_allow_html=True)
        
        
#Trump ordered the deployment of nuclear warheads on the coast of Siberia to halt the Russian troop's advancements towards the shores of Alaska.


