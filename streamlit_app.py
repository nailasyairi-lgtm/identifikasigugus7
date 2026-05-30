import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Organic Chemistry Identifier", 
    page_icon="🌈", 
    layout="centered"
)

# --- HEADER APLIKASI DENGAN WARNA & STYLE ---
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🌈 Smart Lab: Identifikasi Gugus Fungsi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; color: #555555;'>Tebak golongan senyawa organik berdasarkan hasil uji reagen laboratorium secara instan!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- BANNER SELAMAT DATANG ---
st.info("👋 **Halo Analis!** Silakan masukkan data pengamatan dari meja praktikum kamu pada panel di bawah ini, lalu lihat keajaiban analisisnya.")

# --- AREA INPUT (DIBUAT DALAM KOTAK/CONTAINER) ---
with st.container(border=True):
    st.markdown("<h3 style='color: #1E3A8A;'>📋 Hasil Pengamatan Reagen:</h3>", unsafe_allow_html=True)
    
    # Menggunakan Radio Button Horizontal agar lebih visual dan berwarna saat diklik
    uji_lakmus = st.radio(
        "1. Uji Indikator (Kertas Lakmus Biru)",
        ["🔵 Tetap Biru (Netral/Basa)", "🔴 Berubah Menjadi Merah (Asam)"],
        horizontal=True
    )
    
    st.write("") # Jarak
    
    uji_schiff = st.radio(
        "2. Uji Schiff (Identifikasi Spesifik Aldehid)",
        ["⚪ Tidak Bereaksi (Tetap Bening)", "🟣 Positif (Muncul Warna Ungu Kemerahan)"],
        horizontal=True
    )
    
    st.write("") # Jarak
    
    uji_bisulit = st.radio(
        "3. Uji Natrium Bisulfit (Gugus Karbonil)",
        ["🟡 Tidak Terbentuk Endapan", "⚪ Positif (Terbentuk Kristal/Endapan Putih)"],
        horizontal=True
    )

st.markdown("---")

# --- PROSES ANALISIS & OUTPUT OTOMATIS (TANPA TOMBOL AGAR LEBIH INTERAKTIF) ---
st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>🔍 Hasil Analisis Laboratorium</h3>", unsafe_allow_html=True)

# Logika Penentuan Gugus Fungsi (Sistem Pakar Berwarna)

# 1. KONDISI ASAM KARBOKSILAT
if "🔴 Berubah Menjadi Merah" in uji_lakmus:
    st.error("### 🎯 Senyawa: ASAM KARBOKSILAT (—COOH)")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<h1 style='font-size: 80px; text-align: center;'>🧪</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        * **Sifat Kimia:** Bersifat asam lemah. Mampu melepaskan ion $H^+$ yang memutuskan ikatan konjugasi pada lakmus sehingga berubah menjadi merah.
        * **Reaksi Turunan:** Jika direaksikan dengan alkohol + katalis $H_2SO_4$, akan menghasilkan bau harum khas **Ester** (Reaksi Esterifikasi).
        """)
    st.toast("Analisis Berhasil: Asam Karboksilat ditemukan!", icon="🔴")

# 2. KONDISI ALDEHID
elif "🟣 Positif" in uji_schiff:
    st.success("### 🎯 Senyawa: ALDEHID / ALKANAL (—CHO)")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<h1 style='font-size: 80px; text-align: center;'>🍇</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        * **Prinsip Uji Schiff:** Reagen Schiff (Fushsin) yang awalnya terdekolorisasi oleh $SO_2$ akan berikatan kembali dengan gugus fungsi **Aldehid**. Hal ini mengembalikan struktur kromofor reagen sehingga warna **Ungu Kemerahan** muncul kembali.
        * **Uji Pembanding:** Senyawa ini juga pasti positif terhadap uji **Benedict** (endapan merah bata) dan uji **Tollens** (cermin perak).
        """)
    st.toast("Analisis Berhasil: Aldehid ditemukan!", icon="🟣")

# 3. KONDISI KETON
elif "⚪ Positif" in uji_bisulit and "⚪ Tidak Bereaksi" in uji_schiff:
    st.warning("### 🎯 Senyawa: KETON / ALKANON (—CO—)")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("<h1 style='font-size: 80px; text-align: center;'>💎</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        * **Prinsip Uji Bisulfit:** Gugus karbonil pada keton (terutama metil keton) mengalami reaksi **adisi nukleofilik** dengan ion bisulfit ($HSO_3^-$) membentuk garam adisi yang sukar larut, sehingga mengendap sebagai kristal putih.
        * **Kenapa bukan Aldehid?** Karena hasil Uji Schiff menunjukkan warna bening (negatif), mengonfirmasi tidak adanya gugus aldehid bebas.
        """)
    st.toast("Analisis Berhasil: Keton ditemukan!", icon="⚪")

# 4. KONDISI DEFAULT / BELUM SPESIFIK
else:
    st.markdown(
        """
        <div style='background-color: #F0F2F6; padding: 20px; border-radius: 10px; border-left: 5px solid #7E7E7E;'>
            <h4 style='color: #333333; margin-top:0;'>ℹ️ Status: Menunggu Kombinasi Uji Spesifik</h4>
            <p style='color: #555555; margin-bottom:0;'>
                Silakan ubah pilihan reagen di atas. Jika semua hasil bernilai negatif, kemungkinan sampel kamu adalah golongan <b>Alkohol (Alkanol)</b> atau <b>Ester (Alkil Alkanoat)</b> yang bersifat netral.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
