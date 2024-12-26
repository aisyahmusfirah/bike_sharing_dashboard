import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("Dashboard Analisis Data: Bike Sharing Dataset")

# Informasi proyek
st.sidebar.header("Tentang Proyek")
st.sidebar.markdown("""
- **Nama:** Aisyah Musfirah
- **Email:** aishstrawberry@gmail.com
- **ID Dicoding:** aishsahi
""")

# Data Wrangling
st.header("Data Wrangling")

# Load data
import os
file_path = "C:/Users/User/OneDrive/Desktop/Dicoding Spaces/data_analysis_project/day.csv"
if not os.path.exists(file_path):
    print(f"File {file_path} tidak ditemukan!")
else:
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

# Show dataset
if st.checkbox("Tampilkan dataset"):  
    st.write(data.head())

# Dataset summary
st.subheader("Ringkasan Dataset")
st.write("Jumlah missing value per kolom:")
st.write(data.isna().sum())
st.write("Jumlah duplikasi data:", data.duplicated().sum())
st.write("Deskripsi statistik:")
st.write(data.describe())

# Exploratory Data Analysis
st.header("Exploratory Data Analysis (EDA)")

# Pertanyaan 1
st.subheader("Apakah kecepatan angin berpengaruh terhadap jumlah penyewaan sepeda?")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='count', data=data, alpha=0.6, color='blue', ax=ax1)
ax1.set_title('Effect of Windspeed on Bike Rentals', fontsize=14)
ax1.set_xlabel('Windspeed', fontsize=12)
ax1.set_ylabel('Total Rentals (count)', fontsize=12)
st.pyplot(fig1)

correlation = data['windspeed'].corr(data['count'])
st.write(f"Korelasi antara kecepatan angin dan jumlah penyewaan sepeda: {correlation:.2f}")

# Pertanyaan 2
st.subheader("Apakah musim berpengaruh terhadap jumlah penyewaan sepeda?")
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
data['season_label'] = data['season'].map(season_labels)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season_label', y='count', data=data, ax=ax2)
ax2.set_title('Penyewaan Sepeda Berdasarkan Musim', fontsize=14)
ax2.set_xlabel('Musim', fontsize=12)
ax2.set_ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(fig2)

st.write("Keterangan:")
st.markdown("""
- Musim panas memiliki jumlah penyewaan tertinggi.
- Musim dingin memiliki jumlah penyewaan terendah.
""")

# Conclusion
st.header("Kesimpulan")
st.markdown("""
- **Pertanyaan 1:** Terdapat hubungan negatif yang lemah antara kecepatan angin dan jumlah penyewaan sepeda.
- **Pertanyaan 2:** Musim berpengaruh terhadap jumlah penyewaan sepeda. Musim panas dan musim gugur memiliki jumlah penyewaan lebih tinggi dibanding musim lain.
""")
