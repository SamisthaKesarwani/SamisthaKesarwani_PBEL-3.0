import streamlit as st
import numpy as np
from PIL import Image
import tflite_runtime.interpreter as tflite

from class_names import class_names
from disease_info import disease_info, default_info

@st.cache_resource
def load_ai_model():
    interpreter = tflite.Interpreter(model_path="models/crop_disease_model.tflite")
    interpreter.allocate_tensors()
    return interpreter

interpreter = load_ai_model()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

st.set_page_config(
    page_title="Leafie",
    page_icon="🌿",
    layout="wide"
)

st.markdown("""
<style>

/* Simple white background */
.stApp {
    background-color: white;
}

/* Simple result box */
.result-box{
    background:white;
    padding:10px;
    margin-bottom:15px;
}

/* Titles */
.result-title{
    font-size:20px;
    font-weight:bold;
    color:#2E7D32;
    margin-bottom:8px;
}

/* Main values */
.result-text{
    font-size:24px;
    font-weight:bold;
    color:black;
}

/* Information sections */
.info-box{
    background:white;
    padding:10px;
    margin-bottom:12px;
}

/* Section headings */
.info-title{
    color:#2E7D32;
    font-size:20px;
    font-weight:bold;
    margin-bottom:6px;
}

</style>
""", unsafe_allow_html=True)

st.title("🌿 Leafie")
st.write(
    "Upload a photo of a crop leaf and Leafie will try to identify the disease "
    "affecting it, along with its cause, symptoms, and treatment."
)

st.markdown("""
<div class="info-box">
<div class="info-title">🌱 Supported Crops</div>

<b>Apple</b> • <b>Blueberry</b> • <b>Cherry</b> • <b>Corn</b> •
<b>Grape</b> • <b>Orange</b> • <b>Peach</b> • <b>Bell Pepper</b> •
<b>Potato</b> • <b>Raspberry</b> • <b>Soybean</b> •
<b>Squash</b> • <b>Strawberry</b> • <b>Tomato</b>

</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Choose Leaf Images",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    if st.button("Predict Disease"):
        try:
            image = Image.open(uploaded_file).convert("RGB")
        except Exception:
            st.error(f"Cannot read {uploaded_file.name}")
        else:
            img = image.resize((224, 224))
            img = np.array(img).astype("float32")
            img = np.expand_dims(img, axis=0)

            with st.spinner("Analyzing leaf..."):
                interpreter.set_tensor(input_details[0]['index'], img)
                interpreter.invoke()
                prediction = interpreter.get_tensor(output_details[0]['index'])

            predicted_index = np.argmax(prediction)
            confidence = np.max(prediction) * 100

            disease = class_names[predicted_index]

            crop, condition = disease.split("___", 1)

            crop = crop.replace("_", " ").replace(",", "")
            condition = condition.replace("_", " ")

            if "healthy" in condition.lower():
                st.success("✅ Healthy Leaf Detected")
            else:
                st.warning("⚠ Disease Detected")

            info = disease_info.get(disease, default_info)

            col1, col2 = st.columns([1.2, 1.8])

            with col1:
                st.markdown(
                    "<h3 style='text-align:center;'>Uploaded Leaf</h3>",
                    unsafe_allow_html=True
                )
                st.image(image, width=400)

            with col2:

                st.markdown("## 🌿 Prediction Result")

                st.subheader("🎯 Confidence")
                st.write(f"**{confidence:.2f}%**")

                st.subheader("🌿 Prediction")
                st.write(f"**Crop:** {crop}")
                st.write(f"**Disease:** {condition}")

                if confidence >= 90:
                    st.success("🟢 Very High Confidence")
                elif confidence >= 75:
                    st.success("🟢 High Confidence")
                elif confidence >= 60:
                    st.warning("🟡 Moderate Confidence")
                elif confidence >= 40:
                    st.warning("🟠 Low Confidence")
                else:
                    st.error("🔴 Very Low Confidence")
                    st.write(
                        "The model is not very confident about this prediction. "
                        "Please upload a clearer image or capture the leaf under good lighting."
                    )

                st.subheader("🦠 Cause")
                for item in info["cause"]:
                    st.write(f"• {item}")

                st.subheader("🔍 Symptoms")
                for item in info["symptoms"]:
                    st.write(f"• {item}")

                st.subheader("💊 Treatment")
                for item in info["treatment"]:
                    st.write(f"• {item}")

                report = f"""Crop: {crop}

        Disease: {condition}

        Confidence: {confidence:.2f}%

        Cause:
        {chr(10).join(info["cause"])}

        Symptoms:
        {chr(10).join(info["symptoms"])}

        Treatment:
        {chr(10).join(info["treatment"])}
        """

                st.download_button(
                    label="📄 Download Report",
                    data=report,
                    file_name=f"{crop}_report.txt",
                    mime="text/plain"
                )