import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# LOAD DATA & MODEL
df = pd.read_csv('./data/main_data.csv')
model = joblib.load('./model/bike_sharing_rf_model.pkl')


st.title("🚲 Bike Sharing Analysis & Prediction")
st.write("Dashboard ini menyajikan analisis historis peminjaman sepeda dan alat prediksi berbasis Machine Learning.")

# tab 1 untuk visualisasi data dan tab 2 untuk prediksi
tab1, tab2 = st.tabs(["📊 Analisis Data (EDA)", "🤖 Prediksi (Machine Learning)"])

# ==== visualisasi data
with tab1:
    st.header("Exploratory Data Analysis (EDA)")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Transaksi", f"{df['cnt'].sum():,}")
    col2.metric("Rata-rata Harian", f"{int(df['cnt'].mean()):,} Sepeda")
    col3.metric("Rekor Tertinggi", f"{df['cnt'].max():,} Sepeda")

    st.markdown("---")

    col_a, col_b = st.columns(2)

    with col_a:
        st.subheader("Tren Peminjaman Harian")
        fig_trend, ax_trend = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=df, x='dteday', y='cnt', color='skyblue', ax=ax_trend)
        ax_trend.set_title("Jumlah Peminjaman Sepeda (2011-2012)")
        ax_trend.set_xlabel("Tanggal")
        ax_trend.set_ylabel("Jumlah Peminjaman")
        st.pyplot(fig_trend)

    with col_b:
        st.subheader("Peminjaman Berdasarkan Musim")
        fig_season, ax_season = plt.subplots(figsize=(10, 5))

        sns.barplot(data=df, x='season_label', y='cnt', estimator=sum, errorbar=None, 
                    order=['Spring', 'Summer', 'Fall', 'Winter'], palette='viridis', ax=ax_season)
        ax_season.set_title("Total Peminjaman per Musim")
        ax_season.set_xlabel("Musim")
        ax_season.set_ylabel("Total Sepeda")
        st.pyplot(fig_season)

    st.markdown("---")

    col_c, col_d = st.columns(2)

    with col_c:
        st.subheader("Pengaruh Cuaca terhadap Peminjaman")
        fig_weather, ax_weather = plt.subplots(figsize=(10, 5))
        sns.boxplot(data=df, x='weather_label', y='cnt', palette='coolwarm', ax=ax_weather)
        ax_weather.set_title("Distribusi Peminjaman di Berbagai Cuaca")
        st.pyplot(fig_weather)

    with col_d:
        st.subheader("Hubungan Suhu vs Jumlah Peminjaman")
        fig_temp, ax_temp = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df, x='temp', y='cnt', hue='season_label', palette='deep', ax=ax_temp)
        ax_temp.set_title("Scatter Plot: Suhu vs Jumlah Sewa")
        st.pyplot(fig_temp)


# prediksi machine learning
with tab2:
    st.header("Prediksi Peminjaman Sepeda Besok")
    st.write("Gunakan slider di sidebar (sebelah kiri) atau di bawah ini untuk mengatur kondisi.")
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        season = st.selectbox("Musim", (1, 2, 3, 4), format_func=lambda x: {1: "Semi (Spring)", 2: "Panas (Summer)", 3: "Gugur (Fall)", 4: "Dingin (Winter)"}[x])
        mnth = st.slider("Bulan", 1, 12, 1)
        yr = st.radio("Tahun (0=2011, 1=2012)", (0, 1), horizontal=True)
        holiday = st.radio("Hari Libur?", (0, 1), format_func=lambda x: "Tidak" if x == 0 else "Ya", horizontal=True)
        weekday = st.slider("Hari dalam Seminggu (0=Minggu, 6=Sabtu)", 0, 6, 1)
    
    with col_input2:
        workingday = st.radio("Hari Kerja?", (0, 1), format_func=lambda x: "Bukan / Libur" if x == 0 else "Ya, Hari Kerja", horizontal=True)
        weathersit = st.selectbox("Kondisi Cuaca", (1, 2, 3, 4), 
                                      format_func=lambda x: {
                                          1: "Cerah / Sedikit Awan", 
                                          2: "Kabut / Mendung", 
                                          3: "Hujan Ringan / Salju Ringan", 
                                          4: "Hujan Lebat / Badai"
                                      }.get(x, "Unknown"))
        temp = st.slider("Suhu (Normalized)", 0.0, 1.0, 0.5)
        atemp = st.slider("Suhu Terasa (Normalized)", 0.0, 1.0, 0.5)
        hum = st.slider("Kelembaban (Normalized)", 0.0, 1.0, 0.5)
        windspeed = st.slider("Kecepatan Angin (Normalized)", 0.0, 1.0, 0.2)
    
    if st.button("🚀 Prediksi Sekarang", type="primary"):
        data_input = {
            'season': season,
            'yr': yr,
            'mnth': mnth,
            'holiday': holiday,
            'weekday': weekday,
            'workingday': workingday,
            'weathersit': weathersit,
            'temp': temp,
            'atemp': atemp,
            'hum': hum,
            'windspeed': windspeed
        }
        input_df = pd.DataFrame(data_input, index=[0])
        
        prediction = model.predict(input_df)
        result = int(prediction[0])
        
        st.markdown("---")
        st.subheader("Hasil Prediksi:")
        
        col_res1, col_res2 = st.columns([1, 2])
        with col_res1:
            st.metric("Estimasi Sepeda", f"{result} Unit")
        
        with col_res2:
            if result > 4000:
                st.success("🔥 **High Demand!** Persiapkan stok sepeda yang banyak.")
            elif result < 2000:
                st.warning("📉 **Low Demand.** Mungkin hari yang sepi.")
            else:
                st.info("✅ **Normal Demand.** Permintaan standar.")