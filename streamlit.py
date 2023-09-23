import streamlit as st
import scrapy
from scrapy.crawler import CrawlerProcess


# Import your QnA and Sentiment Analysis programs
from qna_bot import qna
from sen_ana import sen_anaz

# Define the Streamlit app
def main():
    st.sidebar.title("Navigation")

    # Add options to the hamburger menu
    app_choice = st.sidebar.radio("Select App", ("QnA", "Sentiment Analysis"))

    if app_choice == "QnA":
        st.title("QnA Program")
        qna()  # Call your QnA program function here

    elif app_choice == "Sentiment Analysis":
        st.title("Sentiment Analysis Program")
        sen_anaz()  # Call your Sentiment Analysis program function here

if __name__ == "__main__":
    main()

