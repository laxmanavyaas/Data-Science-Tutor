import streamlit as st
import google.generativeai as genai

# Set API Key securely
GOOGLE_API_KEY = "Your_Google_API_Key"  # Store in environment variable
if not GOOGLE_API_KEY:
    st.error("API Key is missing! Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=GOOGLE_API_KEY)

# Function to get AI response
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Ensure correct model name
        response = model.generate_content(prompt)
        return response.text if hasattr(response, "text") else "No response received."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Data Science Tutor", layout="wide")
st.title("🤖 Data Science Tutor")

st.sidebar.header("Instructions")
st.sidebar.write(
    """
    - Ask any question related to Data Science, ML, AI, Python, etc.
    - Click the *Submit* button or press *Enter* to get a response.
    """
)

# User input
user_input = st.text_area("Ask a question in Data Science:", "")

if st.button("Submit") and user_input:
    with st.spinner("Thinking... 🤔"):
        response = get_gemini_response(user_input)
    st.success("Response Generated Successfully!")
    st.subheader("AI's Response:")
    st.write(response)

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built with ❤️ using Streamlit & Google Gemini API")
