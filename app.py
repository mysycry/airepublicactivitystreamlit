import streamlit as st

def main():
    st.title("My Chatbot Application")
    
    st.header("Chat with the Bot")
    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            # Here you would typically process the user input and get a response from your chatbot
            # For now, we'll just echo the input
            st.text_area("Bot:", f"You said: {user_input}", height=100)
        else:
            st.warning("Please enter a message.")
    
    st.sidebar.header("About")
    st.sidebar.info("This is a simple chatbot application built with Streamlit.")

if __name__ == "__main__":
    main()
