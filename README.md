# Proyek Analisis Data: Bike Sharing Dataset 🚲

Repository ini berisi proyek analisis data end-to-end menggunakan **Bike Sharing Dataset** sebagai submission GDGoC divisi Machine Learning. Proyek ini mencakup pembersihan data, eksplorasi data (EDA), visualisasi, dan penerapan Machine Learning (Random Forest) yang terintegrasi ke dalam dashboard interaktif menggunakan Streamlit.

## 📁 Struktur File
- `notebook.ipynb`: Jupyter Notebook berisi analisis lengkap (Data Wrangling, EDA) dan proses export data bersih `data_bersih.csv`.
- `train_model.py`: Script python khusus untuk melatih model machine learning dan menyimpannya sebagai file `.pkl`
- `app.py`: Source code utama untuk menjalankan streamlit.
- `day.csv`: Dataset yang digunakan.
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `README.md`: Dokumentasi proyek.

## 📊 Dataset
Dataset yang digunakan adalah **Bike Sharing Dataset** (data harian/`day.csv`). Dataset ini memuat data penyewaan sepeda selama tahun 2011-2012 beserta informasi cuaca dan musim.

Deploy: [Steamlit](https://rillahgdg.streamlit.app/)
Sumber: [Kaggle - Bike Sharing Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset)

## 🚀 Cara Menjalankan

### 1. Setup Environment
Pastikan Anda memiliki Python terinstal. Clone repository ini dan instal dependencies:
```pip install -r requirements.txt```


### 2. Menjalankan Visualisasi Data
Buka `notebook_analysis.ipynb` menggunakan Jupyter Notebook atau VS Code, lalu jalankan semua sel (Run All)
- Langkah ini penting untuk menghasilkan file `data_bersih.csv` untuk training model dan `main_data.csv` visualisasi di streamlit


### 3. Melatih Model Prediksi
Jalankan script training model di terminal untuk menghasilkan model `bike_sharing_rf_model.pkl`
```py training_model.py```

### 4. Menjalankan Dashboard Streamlit
Setelah ketiga langkah di atas selesai, jalankan perintah berikut di terminal untuk membuka halaman web:
```streamlit run app.py```

## 💡 Insight Singkat
1. **Pola Musiman**: Penyewaan sepeda mencapai puncaknya pada musim Gugur (Fall) dan paling rendah pada musim Semi (Spring).
2. **Pengaruh Cuaca**: Suhu memiliki korelasi positif yang kuat dengan jumlah penyewaan. Cuaca cerah mendorong lebih banyak pengguna dibandingkan saat hujan atau salju.
3. **Tren Tahunan**: Terdapat peningkatan signifikan jumlah penyewaan dari tahun 2011 ke 2012, menunjukkan pertumbuhan popularitas layanan.

## 👤 Profil
- **Nama**: Duhairillah
- **Jurusan**: Teknik Informatika