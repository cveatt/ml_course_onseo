import streamlit as st

from modules.simple_ml_models import SentimentModel


@st.cache
def load_model():
    print("Load model...")
    return SentimentModel()


    if __name__ == "__main__":
        sentiment_model = load_model()
        sentiment_map = {
            1: "Positive",
            0: "Neutral",
            -1: "Negative"
        }

        st.title("SentimentModel")
        
        with st.form("my_form"):
            text = st.text_area("text")

            submitted = st.form_submit_button("Submit")
            if submitted:
                sentiment = sentiment_model(text=text)
                st.write(f"Sentiment: {sentiment_map[sentiment]}")

                if sentiment == 1:
                    st.balloons()
                    