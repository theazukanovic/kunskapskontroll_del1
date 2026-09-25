import streamlit as st
import numpy as np
from PIL import Image
from joblib import load

model = load("extra_trees_mnist.joblib")
scaler = load("mnist_scaler.joblib")

st.title("Sifferigenkänning")
st.write(
    "Ladda upp en bild på en handskriven siffra " "så försöker modellen känna igen den."
)

uploaded_file = st.file_uploader("Välj en bild", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("L")
    img = img.resize((28, 28))

    img_array = np.array(img).astype(np.float64)
    img_flat = img_array.reshape(1, -1)

    img_scaled = scaler.transform(img_flat)
    prediction = model.predict(img_scaled)[0]

    st.image(img, caption="Bearbetad bild", width=200)
    st.success(f"Modellen tror att siffran är: {prediction}")
