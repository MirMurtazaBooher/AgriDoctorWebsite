import streamlit as st
import requests

# ----------------- CONFIG -----------------
BACKEND_URL = "http://127.0.0.1:8000/chat"
API_KEY = "kc_live_8f29a1c3d7b44e9aa62f"  # ← paste the key generated from /generate-api-key
# ------------------------------------------

st.set_page_config(page_title="KissanConnect", page_icon="🌾")

st.title("🌾 KissanConnect")
st.subheader("Agriculture & Crop Disease Advisor")

st.markdown("Ask questions about crops, diseases, treatment, and prevention.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask your agriculture question...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    try:
        response = requests.post(
            BACKEND_URL,
            params={"question": user_input},
            headers={"X-API-KEY": API_KEY},
            timeout=20
        )

        if response.status_code == 200:
            bot_reply = response.json()["answer"]
        else:
            bot_reply = f"❌ Backend error: {response.text}"

    except Exception as e:
        bot_reply = f"❌ Connection error: {str(e)}"

    # Save assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
