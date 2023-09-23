import streamlit as st
import subprocess
from qna_bot import qna
from sen_ana import sen_anaz

# Define the Streamlit app
def main():
    st.sidebar.title("Navigation")

    # Add options to the hamburger menu
    app_choice = st.sidebar.radio("Select App", ("QnA", "Sentiment Analysis"))

    if app_choice == "QnA":
        st.title("QnA Program")
        
        # Add a text input field for the Amazon link
        amazon_link = st.text_input("Enter Amazon Link:")
        
        if amazon_link:
            # Add a button to trigger web scraping with the Amazon link
            if st.button("Submit Link"):
                # Run Scrapy in a separate process
                subprocess.Popen(["python", "scrapy_spider.py",amazon_link])

            user_question = st.text_input("Ask a Question:")
            
            if user_question:
                # Add a button to trigger QnA with the user's question
                if st.button("Get Answer"):
                    # You can retrieve the answer from a file or other IPC mechanisms
                    with open('bot_input', 'r') as f:
                        answer = qna(user_question)
                    st.write(f" {answer}")  # Display the answer in Streamlit

    elif app_choice == "Sentiment Analysis":
        st.title("Sentiment Analysis Program")
        
        # Add a text area for user reviews
        user_review = st.text_area("Enter a Review:")
        
        if user_review:
            # Add a button to trigger the Sentiment Analysis program
            if st.button("Analyze Sentiment"):
                # Call your Sentiment Analysis program function with the input
                # sentiment_result = sen_anaz(user_review)  # Replace with your actual function
                sentiment_result = sen_anaz(user_review) # Replace with the actual result
                st.write(f"Sentiment: {sentiment_result}")  # Display the sentiment result in Streamlit

if __name__ == "__main__":
    main()
