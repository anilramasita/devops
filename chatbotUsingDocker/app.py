import streamlit as st
from chatbot import chat_with_gemini

def main():
    st.title("🤖 Gemini Chatbot")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    user_input = st.text_input("You:", "", key="user_input")
    
    if st.button("Send") and user_input:
        response = chat_with_gemini(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))
    
    st.subheader("Chat History")
    for role, text in st.session_state.chat_history:
        st.write(f"**{role}:** {text}")

if __name__ == "__main__":
    main()
