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

# Pertanyaan 1
st.subheader("1. Bagaimana rata-rata penyewaan sepeda berdasarkan musim?")
# Mapping season ke nama musim
data['season_name'] = data['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# Membuat plot
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
plt.show()

st.write("Kesimpulan:")
st.markdown("""
- Terdapat perbedaan jumlah penyewaan tiap musim
- Musim gugur (fall) memiliki jumlah penyewaan tertinggi dibanding musim lainnya
- Musim semi (spring) memiliki jumlah penyewaan paling rendah
            """)
 
# Pertanyaan 2
# Boxplot jumlah penyewaan berdasarkan cuaca
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x="weather", y="count")
plt.title("Pengaruh Cuaca terhadap Jumlah Penyewaan Sepeda", fontsize=14)
plt.xlabel("Cuaca (weather)", fontsize=12)
plt.ylabel("Jumlah Penyewaan (count)", fontsize=12)
plt.xticks(ticks=[0, 1, 2, 3], labels=["Cerah", "Berawan", "Hujan Ringan", "Hujan Deras"])
plt.show()

st.write("Kesimpulan:")
st.markdown("""
- Boxplot menunjukkan bahwa cuaca cerah cenderung memiliki jumlah penyewaan sepeda yang lebih tinggi dan lebih bervariasi dibandingkan cuaca lainnya
- Cuaca hujan deras cenderung memiliki jumlah penyewaan terendah
""")
