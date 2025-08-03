import streamlit as st
import requests

from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent" , layout="centered")
st.title("Multi AI Agent using Groq and Tavily New")


st.markdown("### Define your AI Agent:")
prompt_options = [
    "You are a career counselor for CS students.",
    "You are a coding tutor specializing in DSA.",
    "You are an AI that summarizes news articles.",
    "You are a helpful assistant for job preparation.",
    "You are a full-stack mentor helping with project ideas.",
    "You are an AI for tech interview mock sessions.",
    "You are a resume-building expert.",
    "You are a startup advisor for tech students.",
    "You are an academic planner for engineering students.",
    "You are an AI that explains tough coding concepts."
]

system_prompt = st.selectbox("Select or scroll through predefined roles:", prompt_options)

selected_model = st.selectbox("Select your AI model: ", settings.ALLOWED_MODEL_NAMES)

allow_web_search = st.checkbox("Allow web search")

user_query = st.text_area("Enter your query : " , height=150)

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent") and user_query.strip():

    payload = {
        "model_name" : selected_model,
        "system_prompt" : system_prompt,
        "messages" : [user_query],
        "allow_search" : allow_web_search
    }

    try:
        logger.info("Sending request to backend")

        response = requests.post(API_URL , json=payload)

        if response.status_code==200:
            agent_response = response.json().get("response","")
            logger.info("Sucesfully recived response from backend")

            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n","<br>"), unsafe_allow_html=True)

        else:
            logger.error("Backend error")
            st.error("Error with backend")
    
    except Exception as e:
        logger.error("Error occured while sending request to backend")
        st.error(str(CustomException("Failed to communicate to backend")))

        