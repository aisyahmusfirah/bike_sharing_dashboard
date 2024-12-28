import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Dashboard Analisis Data: Bike Sharing Dataset")

# Exploratory Data Analysis
st.header("Exploratory Data Analysis (EDA)")

# Load Data
file_path = "data/day.csv"

@st.cache
def load_data(file_path):
    data = pd.read_csv(file_path)
    data = data.rename(columns={
        'yr': 'year',
        'mnth': 'month',
        'hum': 'humidity',
        'weathersit': 'weather',
        'cnt': 'count',
        'hr': 'hour'
    })
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

data = load_data(file_path)

# Filtering berdasarkan cuaca (weather)
weather_options = {
    1: 'Cerah',
    2: 'Berawan',
    3: 'Hujan Ringan',
    4: 'Hujan Deras'
}

# Dropdown untuk memilih cuaca
selected_weather = st.selectbox(
    "Pilih Cuaca untuk Filter Data:",
    options=list(weather_options.values())
)

# Mapping weather ke kode numerik
weather_code = {v: k for k, v in weather_options.items()}
filtered_data = data[data['weather'] == weather_code[selected_weather]]

# Pertanyaan 1: Analisis berdasarkan cuaca yang dipilih
st.subheader(f"1. Pengaruh Cuaca ({selected_weather}) terhadap Penyewaan Sepeda")

# Plot boxplot berdasarkan cuaca yang dipilih
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x="weather", y="count")
plt.title(f"Pengaruh Cuaca {selected_weather} terhadap Jumlah Penyewaan Sepeda", fontsize=14)
plt.xlabel("Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewaan Sepeda", fontsize=12)
plt.xticks(ticks=[0, 1, 2, 3], labels=["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"])
st.pyplot(plt)

# Pertanyaan 2: Rata-rata penyewaan sepeda berdasarkan musim
st.subheader("2. Rata-rata Penyewaan Sepeda Berdasarkan Musim")

# Mapping season ke nama musim
data['season_name'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Membuat plot rata-rata penyewaan sepeda per musim
sns.barplot(
    data=filtered_data, 
    x="season_name", 
    y="count", 
    estimator="mean",
    ci=None, 
    palette="coolwarm"
)
plt.title("Rata-rata Penggunaan Sepeda di Setiap Musim")
plt.xlabel("Musim")
plt.ylabel("Jumlah Penggunaan Sepeda (Rata-rata)")
st.pyplot(plt)

st.write("Kesimpulan:")
st.markdown(""" 
- Terdapat perbedaan jumlah penyewaan berdasarkan cuaca
- Cuaca cerah cenderung memiliki jumlah penyewaan yang lebih tinggi dibandingkan cuaca lainnya
""")
