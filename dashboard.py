import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)


@st.cache_data
def load_data():
    # Pastikan file day.csv ada di folder yang sama
    try:
        df = pd.read_csv('day.csv')
        
        # Cleaning & Mapping
        df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
        df['year_label'] = df['yr'].map({0: '2011', 1: '2012'})
        df['weather_label'] = df['weathersit'].map({
            1: 'Clear/Partly Cloudy',
            2: 'Misty/Cloudy',
            3: 'Light Snow/Rain',
            4: 'Severe Weather'
        })
        df['dteday'] = pd.to_datetime(df['dteday'])
        return df
    except FileNotFoundError:
        st.error("File 'day.csv' tidak ditemukan. Harap unduh dataset Bike Sharing dan letakkan di folder ini.")
        return None
    
df = load_data()

if df is not None:
    st.sidebar.title("Filter Data")

    # Filter Tahun
    selected_year = st.sidebar.multiselect(
        "Pilih Tahun",
        options=df['year_label'].unique(),
        default=df['year_label'].unique()
    )
    
    # Filter Musim
    selected_season = st.sidebar.multiselect(
        "Pilih Musim",
        options=df['season_label'].unique(),
        default=df['season_label'].unique()
    )

    # Filter Data berdasarkan pilihan
    filtered_df = df[
        (df['year_label'].isin(selected_year)) &
        (df['season_label'].isin(selected_season))
    ]

    st.title("🚲 Dashboard Analisis Bike Sharing")
    st.markdown("Dashboard ini menampilkan insight dari dataset penyewaan sepeda, termasuk pengaruh musim dan cuaca.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Penyewaan", value=f"{filtered_df['cnt'].sum():,}")
    with col2:
        st.metric("Rata-rata Suhu (Norm)", value=f"{filtered_df['temp'].mean():.2f}")
    with col3:
        st.metric("Hari Terbanyak", value=filtered_df.loc[filtered_df['cnt'].idxmax(), 'dteday'].strftime('%Y-%m-%d'))

    st.divider()

    # --- Visualisasi 1 & 2 (Side by Side) ---
    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.subheader("Rata-rata Sewa per Musim")
        # Agregasi data
        season_avg = filtered_df.groupby('season_label')['cnt'].mean().reset_index()
        
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.barplot(data=season_avg, x='season_label', y='cnt', palette='viridis', ax=ax1)
        ax1.set_xlabel("Musim")
        ax1.set_ylabel("Rata-rata Sewa")
        st.pyplot(fig1)

    with col_chart2:
        st.subheader("Tren Penyewaan vs Suhu")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=filtered_df, x='temp', y='cnt', hue='season_label', alpha=0.6, ax=ax2)
        ax2.set_xlabel("Suhu (Normalized)")
        ax2.set_ylabel("Jumlah Sewa")
        st.pyplot(fig2)

    st.divider()

    # --- Fitur Tambahan: Prediksi Sederhana (ML) ---
    st.subheader("🤖 Prediksi Jumlah Sewa (Machine Learning Demo)")
    st.markdown("Masukkan kondisi cuaca untuk memprediksi jumlah penyewaan sepeda harian.")

    # Input User
    col_input1, col_input2, col_input3 = st.columns(3)
    with col_input1:
        input_temp = st.slider("Suhu (Normalized 0-1)", 0.0, 1.0, 0.5)
    with col_input2:
        input_hum = st.slider("Kelembaban (Normalized 0-1)", 0.0, 1.0, 0.5)
    with col_input3:
        input_wind = st.slider("Kecepatan Angin (Normalized 0-1)", 0.0, 1.0, 0.2)

    # Train Model on the fly (Simple implementation)
    X = df[['temp', 'hum', 'windspeed']]
    y = df['cnt']
    model = LinearRegression()
    model.fit(X, y)
    
    prediction = model.predict([[input_temp, input_hum, input_wind]])[0]

    st.success(f"Prediksi Jumlah Penyewaan Sepeda: **{int(prediction)} unit**")
    
    # --- Checkbox Data Raw ---
    if st.checkbox("Tampilkan Data Mentah"):
        st.write(filtered_df)

else:
    st.info("Menunggu file dataset...")