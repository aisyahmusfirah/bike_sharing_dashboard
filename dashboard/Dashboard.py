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

# Menampilkan dataset yang sudah di-describe
st.header("Statistik Deskriptif dari Dataset")
st.dataframe(data.describe())

# Pertanyaan 1: Analisis berdasarkan cuaca yang dipilih
st.subheader(f"1. Pengaruh Cuaca terhadap Penyewaan Sepeda")

# Pilihan cuaca (weather)
weather_options = {
    0: 'All Weather',
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

if weather_code[selected_weather] == 0:  # Jika "All Weather" dipilih
    filtered_data = data
    st.write("Menampilkan semua data cuaca.")
else:
    filtered_data = data[data['weather'] == weather_code[selected_weather]]
    st.write(f"Menampilkan data untuk cuaca: {selected_weather}")

# Plot boxplot berdasarkan cuaca yang dipilih
plt.figure(figsize=(10, 6))
sns.boxplot(data=filtered_data, x="weather", y="count", width=0.5)
plt.title(f"Pengaruh Cuaca {selected_weather} terhadap Jumlah Penyewaan Sepeda", fontsize=14)
plt.xlabel("Cuaca", fontsize=12)
plt.ylabel("Jumlah Penyewaan Sepeda", fontsize=12)
# Tampilkan plot di Streamlit
st.pyplot(plt)

# Pertanyaan 2: Rata-rata penyewaan sepeda berdasarkan musim
st.subheader("2. Rata-rata Penyewaan Sepeda Berdasarkan Musim")

# Mapping season ke nama musim
data['season_name'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Membuat plot rata-rata penyewaan sepeda per musim
plt.figure(figsize=(10, 6))
sns.barplot(
    data=data, 
    x="season_name", 
    y="count", 
    estimator="mean",
    ci=None, 
    palette="coolwarm"
)
plt.title("Rata-rata Penggunaan Sepeda di Setiap Musim")
plt.xlabel("Musim")
plt.ylabel("Jumlah Penggunaan Sepeda (Rata-rata)")

# Tampilkan plot di Streamlit
st.pyplot(plt)

# Kesimpulan
st.write("Kesimpulan:")
st.markdown(""" 
- **Pertanyaan 1:** Cuaca cerah (Clear) cenderung memiliki jumlah penyewaan tertinggi, sementara cuaca hujan deras (Heavy Rain) memiliki jumlah penyewaan terendah. Kondisi cuaca seperti hujan ringan (Light Snow/Rain) dan berawan (Mist/Cloudy) berada di antara keduanya. Hal ini menunjukkan bahwa masyarakat cenderung lebih memilih menggunakan layanan bike sharing saat cuaca cerah dan menghindari penggunaannya saat cuaca buruk.
            
- **Pertanyaan 2:** Musim gugur (Fall) memiliki rata-rata penyewaan sepeda tertinggi, diikuti oleh musim panas (Summer), musim dingin (Winter), dan terakhir musim semi (Spring) dengan rata-rata penyewaan terendah. Hal ini menunjukkan bahwa faktor musim memiliki pengaruh terhadap minat masyarakat dalam menggunakan layanan bike sharing.
            """)


