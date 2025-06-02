import streamlit as st
import requests

st.title("Personality Prediction App")

st.markdown("""
Predict whether someone is an **Introvert** or **Extrovert** based on their social behavior.
""")

# Input fields
Time_spent_Alone = st.number_input("Time Spent Alone (hours)", min_value=0, max_value=24, value=3)
Stage_fear = st.selectbox("Stage Fear (Yes=1, No=0)", options=[0, 1], format_func=lambda x: "Yes" if x==1 else "No")
Social_event_attendance = st.number_input("Social Event Attendance (count)", min_value=0, max_value=100, value=5)
Going_outside = st.number_input("Going Outside (hours per day)", min_value=0, max_value=24, value=4)
Drained_after_socializing = st.selectbox("Drained After Socializing (Yes=1, No=0)", options=[0, 1], format_func=lambda x: "Yes" if x==1 else "No")
Friends_circle_size = st.number_input("Friends Circle Size", min_value=0, max_value=1000, value=10)
Post_frequency = st.number_input("Post Frequency (per day)", min_value=0, max_value=100, value=3)

if st.button("Predict Personality"):
    # Prepare JSON payload
    data = {
        "Time_spent_Alone": Time_spent_Alone,
        "Stage_fear": Stage_fear,
        "Social_event_attendance": Social_event_attendance,
        "Going_outside": Going_outside,
        "Drained_after_socializing": Drained_after_socializing,
        "Friends_circle_size": Friends_circle_size,
        "Post_frequency": Post_frequency
    }

    try:
        # Replace URL with your FastAPI backend URL if not localhost
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        result = response.json()

        if response.status_code == 200:
            st.success(f"Prediction: **{result['prediction']}**")
        else:
            st.error(f"Error: {result}")

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
