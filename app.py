import streamlit as st
from langchain_pipeline.pipeline import get_openai_response

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Streamlit Azure OpenAI Integration")

# Get user input
user_input = st.text_input("Enter your query:")

if user_input:
    # Get response from OpenAI through Langchain
    response = get_openai_response(user_input)
    
    # Display the response
    st.write("Azure OpenAI response:")
    st.write(response)
