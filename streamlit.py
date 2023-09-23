import streamlit as st
from qna_bot import qna, run_crawler
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
            if st.button("Scrape Amazon"):
                run_crawler(amazon_link)  # Call the modified function to scrape Amazon

            # Add a text input field for user questions
            user_question = st.text_input("Ask a Question:")
            
            if user_question:
                # Add a button to trigger QnA with the user's question
                if st.button("Get Answer"):
                    answer = qna(user_question)  # Call the modified function to get answers
                    st.write(f"Answer: {answer}")  # Display the answer in Streamlit

    elif app_choice == "Sentiment Analysis":
        st.title("Sentiment Analysis Program")
        
        # Add a text area for user reviews
        user_review = st.text_area("Enter a Review:")
        
        if user_review:
            # Add a button to trigger the Sentiment Analysis program
            if st.button("Analyze Sentiment"):
                sentiment_result = sen_anaz(user_review)  # Call your Sentiment Analysis program function with the input
                st.write(f"Sentiment: {sentiment_result}")  # Display the sentiment result in Streamlit

if __name__ == "__main__":
    main()
