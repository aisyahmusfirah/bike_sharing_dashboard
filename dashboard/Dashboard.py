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

# 1. Pengaruh Kecepatan Angin terhadap Jumlah Penyewaan Sepeda
st.subheader("1. Pengaruh Kecepatan Angin terhadap Jumlah Penyewaan Sepeda")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='windspeed', y='count', data=data, alpha=0.6, color='blue', ax=ax1)
ax1.set_title('Effect of Windspeed on Bike Rentals', fontsize=14)
ax1.set_xlabel('Windspeed', fontsize=12)
ax1.set_ylabel('Total Rentals (count)', fontsize=12)
st.pyplot(fig1)

correlation = data['windspeed'].corr(data['count'])
st.write(f"Korelasi antara kecepatan angin dan jumlah penyewaan sepeda: {correlation:.2f}")

st.write("Kesimpulan:")
st.markdown("""
Terdapat hubungan negatif yang lemah antara kecepatan angin dan jumlah penyewaan sepeda. Artinya jumlah penyewaan sepeda berkurang ketika
            angin berhembus kencang, namun pengaruhnya tidak terlalu signifikan.
            """)
 
# 2. Pengaruh Musim terhadap Jumlah Penyewaan Sepeda
st.subheader("2. Pengaruh Musim terhadap Jumlah Penyewaan Sepeda")
season_labels = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
data['season_label'] = data['season'].map(season_labels)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='season_label', y='count', data=data, ax=ax2)
ax2.set_title('Penyewaan Sepeda Berdasarkan Musim', fontsize=14)
ax2.set_xlabel('Musim', fontsize=12)
ax2.set_ylabel('Jumlah Penyewaan', fontsize=12)
st.pyplot(fig2)

st.write("Kesimpulan:")
st.markdown("""
Musim berpengaruh terhadap jumlah penyewaan sepeda. 
            Musim panas dan musim gugur memiliki jumlah penyewaan lebih tinggi dibanding musim lain.
            Dalam artian pelanggan lebih menyukai bersepeda ketika musim panas dan musim gugur, dan
            menghindari bersepeda ketika musim dingin dan musim semi.
""")
