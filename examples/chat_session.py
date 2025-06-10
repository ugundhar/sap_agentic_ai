import streamlit as st
import groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="Groq Qwen Chatbot",
    page_icon="💬",
    layout="wide"
)

# Initialize Groq client
@st.cache_resource
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("GROQ_API_KEY not found. Please set it in your .env file.")
        st.stop()
    return groq.Client(api_key=api_key)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your AI assistant powered by Groq's Qwen model. How can I help you today?"}
    ]

# Display chat header
st.title("💬 Groq Qwen Chatbot")
st.caption("Chat with Groq's Qwen model")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate response
def generate_response(prompt):
    client = get_groq_client()
    
    # Prepare the messages for the API
    messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
    
    try:
        # Call the Groq API with Qwen model
        chat_completion = client.chat.completions.create(
            model="qwen-qwq-32b",  # Using Qwen model
            messages=messages,
            temperature=0.7,
            max_tokens=1024,
        )
        
        # Extract and return the response
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with a spinner while generating
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
   
       ```
    """)
    
    # Add a clear conversation button
    if st.button("Clear Conversation"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! I'm your AI assistant powered by Groq's Qwen model. How can I help you today?"}
        ]
        st.rerun()