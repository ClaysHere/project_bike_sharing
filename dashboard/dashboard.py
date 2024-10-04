import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set_theme(style='dark')

st.header('Bike Sharing :sparkles:')

def create_sum_by_season_day(df):
    jumlah_penyewa = df.groupby('season_day')['cnt_day'].mean()
    return jumlah_penyewa

all_df = pd.read_csv("./all_data.csv")

all_df["dteday"] = pd.to_datetime(all_df["dteday"])

min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()


with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("./bike.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
   
    
main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

jumlah_penyewa = create_sum_by_season_day(all_df)

# Membuat bar plot dengan matplotlib
st.header('Keterkaitan Musim dan Jumlah Penyewa')
fig, ax = plt.subplots()
ax.bar(jumlah_penyewa.index, jumlah_penyewa.values)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Jumlah Penyewa Dalam Sehari')

# Menampilkan plot ke Streamlit
st.pyplot(fig)

# Membuat subplot dengan 2 kolom
tab1, tab2 = st.tabs(["Pola Berdasarkan Bulan", "Pola Berdasarkan Jam"])

# Plot pertama: Pola jumlah penyewa berdasarkan bulan
with tab1:
    st.header("Pola Jumlah Penyewa Berdasarkan Bulan")
    plt.figure(figsize=(20, 8))
    sns.lineplot(x="mnth_day", y="cnt_day", data=all_df, errorbar=None)  # Ganti ci dengan errorbar
    plt.ylabel("Jumlah Penyewa Harian", fontsize=18)
    plt.xlabel("Bulan", fontsize=18)
    plt.title("Pola Jumlah Penyewa Berdasarkan Bulan", fontsize=22)

    # Menyesuaikan ukuran font untuk ticks (nilai)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    # Mengubah ukuran font label untuk nilai pada sumbu Y
    for tick in plt.gca().get_yticklabels():
        tick.set_fontsize(16)  # Ukuran font untuk label ticks sumbu Y

    st.pyplot(plt.gcf())  # Menampilkan plot ke dalam tab pertama

# Plot kedua: Pola jumlah penyewa berdasarkan jam
with tab2:
    st.header("Pola Jumlah Penyewa Berdasarkan Jam")
    plt.figure(figsize=(20, 8))
    sns.lineplot(x="hr", y="cnt_hour", data=all_df, errorbar=None)  # Ganti ci dengan errorbar
    plt.ylabel("Jumlah Penyewa Harian", fontsize=18)
    plt.xlabel("Jam", fontsize=18)
    plt.title("Pola Jumlah Penyewa Berdasarkan Jam", fontsize=22)

    # Menyesuaikan ukuran font untuk ticks (nilai)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    # Mengubah ukuran font label untuk nilai pada sumbu Y
    for tick in plt.gca().get_yticklabels():
        tick.set_fontsize(16)  # Ukuran font untuk label ticks sumbu Y

    st.pyplot(plt.gcf())  # Menampilkan plot ke dalam tab kedua