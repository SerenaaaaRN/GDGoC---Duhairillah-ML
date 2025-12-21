# Proyek Analisis Data: Bike Sharing Dataset 🚲

Repository ini berisi proyek analisis data end-to-end menggunakan **Bike Sharing Dataset**. Proyek ini mencakup pembersihan data, eksplorasi data (EDA), visualisasi, dan dashboard interaktif menggunakan Streamlit.

## 📁 Struktur File
- `notebook.ipynb`: Jupyter Notebook berisi analisis lengkap (Data Wrangling, EDA, Visualisasi).
- `dashboard.py`: Source code untuk dashboard interaktif Streamlit.
- `day.csv`: Dataset yang digunakan (harus diunduh terpisah).
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `README.md`: Dokumentasi proyek.

## 📊 Dataset
Dataset yang digunakan adalah **Bike Sharing Dataset** (data harian/`day.csv`). Dataset ini memuat data penyewaan sepeda selama tahun 2011-2012 beserta informasi cuaca dan musim.

Sumber: [Kaggle](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

## 🚀 Cara Menjalankan

### 1. Setup Environment
Pastikan Anda memiliki Python terinstal. Clone repository ini dan instal dependencies:
```pip install -r requirements.txt```


### 2. Menjalankan Notebook
Buka Jupyter Notebook atau VS Code untuk menjalankan analisis:
```jupyter notebook notebook_analysis.ipynb```

### 3. Menjalankan Dashboard Streamlit
Untuk melihat dashboard interaktif, jalankan perintah berikut di terminal:
```streamlit run app.py```

## 💡 Insight Singkat
1. **Pola Musiman**: Penyewaan sepeda mencapai puncaknya pada musim Gugur (Fall) dan paling rendah pada musim Semi (Spring).
2. **Pengaruh Cuaca**: Suhu memiliki korelasi positif yang kuat dengan jumlah penyewaan. Cuaca cerah mendorong lebih banyak pengguna dibandingkan saat hujan atau salju.
3. **Tren Tahunan**: Terdapat peningkatan signifikan jumlah penyewaan dari tahun 2011 ke 2012, menunjukkan pertumbuhan popularitas layanan.

## 👤 Profil
**Nama**: Duhairillah
**Jurusan**: Teknik Informatika