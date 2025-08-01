import streamlit as st
import numpy as np
import joblib  

# Set layout to wide to stretch content
st.set_page_config(layout="wide")

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  

st.title("Smart Sprinkler System -- By : Deepti Chincholi")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")

# Collect sensor inputs (scaled values)
sensor_values = []

# Create sliders in rows of 5 columns
for i in range(0, 20, 5):
    cols = st.columns(5)
    for j in range(5):
        if i + j < 20:
            with cols[j]:
                val = st.slider(f"Sensor {i + j}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
                sensor_values.append(val)

# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.write(f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")
