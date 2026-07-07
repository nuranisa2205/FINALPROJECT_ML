import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model_kelulusan.pkl")

st.set_page_config(
    page_title="Prediksi Kelulusan",
    page_icon="🎓"
)

st.title("🎓 Prediksi Kelulusan Mahasiswa")
st.write("Menggunakan Algoritma Random Forest")

# Input
gpa = st.number_input(
    "Nilai GPA",
    min_value=0.0,
    max_value=4.0,
    value=0.0
)

absences = st.number_input(
    "Jumlah Ketidakhadiran",
    min_value=0,
    max_value=30,
    value=0
)

study_time = st.number_input(
    "Jam Belajar per Minggu",
    min_value=0.0,
    max_value=25.0,
    value=0.0
)

# Data input
input_data = pd.DataFrame({
    'GPA': [gpa],
    'Absences': [absences],
    'StudyTimeWeekly': [study_time]
})

# Prediksi
if st.button("Prediksi"):

    hasil = model.predict(input_data)

    if hasil[0] == 1:
        st.success("✅ Diprediksi Lulus")
    else:
        st.error("❌ Diprediksi Tidak Lulus")