import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Customizable AI Tutor Character
def get_tutor_character():
    st.sidebar.title("Customize Your Tutor")
    name = st.sidebar.text_input("Name your tutor:", value="Codey")
    interests = st.sidebar.multiselect(
        "What are your interests?",
        ["Robots", "Space", "Dinosaurs", "Superheroes", "Animals"],
        default=["Robots"]
    )
    return name, interests

# AI Tutor Function
def python_tutor(prompt, name, interests):
    interests_str = ", ".join(interests)
    system_message = f"""
    You are a friendly Python tutor named {name}. Your goal is to teach children basic Python programming in a fun and engaging way.
    The child is interested in {interests_str}. Use these interests to make examples and explanations relatable.
    Keep your responses short, simple, and easy to understand.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Choose the appropriate model
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response['choices'][0]['message']['content'].strip()
# Streamlit App
def main():
    st.title("PythonPal: Your AI-Powered Python Tutor 🐍")
    st.write("""
    Welcome to PythonPal! This app helps kids learn Python programming in a fun and interactive way. 
    Customize your AI tutor, ask questions, and complete interactive exercises to become a Python pro!
    """)

    # Customize Tutor
    tutor_name, tutor_interests = get_tutor_character()
    st.sidebar.write(f"Your tutor, {tutor_name}, is ready to help you learn Python!")

    # User Input
    user_input = st.text_input("Ask your tutor a question or type 'start' to begin:")

    if user_input:
        if user_input.lower() == "start":
            st.write(f"{tutor_name}: Hi! I'm {tutor_name}, your Python tutor. Let's learn some Python together! What do you want to know?")
        else:
            response = python_tutor(user_input, tutor_name, tutor_interests)
            st.write(f"{tutor_name}: {response}")

    # Interactive Homework Assignment
    st.header("Interactive Homework 🎯")
    st.write("Let's practice what you've learned!")
    st.write("**Question:** Write a Python program to print 'Hello, World!'")
    user_code = st.text_area("Write your code here:")
    if st.button("Run Code"):
        if "print('Hello, World!')" in user_code:
            st.success("Great job! You got it right! 🎉")
        else:
            st.error("Almost there! Try again. Remember to use `print('Hello, World!')`.")

if __name__ == "__main__":
    main()
