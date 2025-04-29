import os
import json
import httpx
import streamlit as st
import asyncio
# Configuration
BACKEND_API_URL = os.environ.get("BACKEND_API_URL", "http://localhost:8000")

# Set page config
st.set_page_config(
    page_title="Chat with Gemma",
    page_icon="💬",
    layout="wide",
)

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "ai", "content": "Hello! How can I help you today?"}
    ]

# Display title
st.title("Chat with Gemma 3 (4B-IT)")

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] != "system":  # Don't display system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Function to send message to backend API
async def send_message(messages, temperature=0.5, model="gemma3:1b-it-q4_K_M"):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{BACKEND_API_URL}/llm/chat",
                json={
                    "messages": messages,
                    "temperature": temperature,
                    "model": model
                },
                timeout=60.0  # Longer timeout for model inference
            )
        
        if response.status_code == 200:
            return response.json()["content"]
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return "Sorry, I encountered an error. Please try again."
    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        return "Sorry, I couldn't connect to the backend service. Please check if it's running."

# Sidebar for settings
with st.sidebar:
    st.title("Settings")
    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    
    # Add a button to clear chat history
    if st.button("Clear Chat"):
        st.session_state.messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "ai", "content": "Hello! How can I help you today?"}
        ]
        st.rerun()

# Chat input area
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "human", "content": prompt})
    
    # Display user message
    with st.chat_message("human"):
        st.markdown(prompt)
    
    # Display assistant response with a spinner
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            # Send message to API and get response
            response = asyncio.run(send_message(st.session_state.messages, temperature))
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "ai", "content": response})