import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(page_title="Organic Group Identifier", page_icon="🧪", layout="centered")

# Desain Header
st.title("🧪 Kimia Organik: Gugus Fungsi Identifier")
st.write("Aplikasi pembantu analis untuk mengidentifikasi gugus fungsi sampel organik berdasarkan hasil uji reagen laboratorium.")
st.markdown("---")

# Input Data Hasil Uji Lab oleh Analis
st.subheader("📋 Masukkan Hasil Pengamatan Uji Lab:")

col1, col2 = st.columns(2)

with col1:
    # 1. Uji Unsur / Sifat Umum
    uji_kelarutan = st.selectbox("Kelarutan dalam Air:", ["Larut", "Tidak Larut"])
    
    # 2. Uji Reagen Spesifik Aldehid/Keton
    uji_schiff = st.selectbox("Uji Schiff (Identifikasi Aldehid):", [
        "Tidak Bereaksi (Tetap Bening)", 
        "Positif (Muncul Warna Ungu Kemerahan)"
    ])

with col2:
    # 3. Uji Reagen Karbonil Umum
    uji_bisulit = st.selectbox("Uji Natrium Bisulfit:", [
        "Tidak Terbentuk Endapan", 
        "Positif (Terbentuk Kristal/Endapan Putih)"
    ])
    
    # 4. Uji Lakmus / Keasaman
    uji_lakmus = st.selectbox("Uji Kertas Lakmus Biru:", [
        "Tetap Biru (Netral/Basa)", 
        "Berubah Menjadi Merah (Asam)"
    ])

st.markdown("---")

# Tombol Eksekusi Analisis
if st.button("🔍 Jalankan Analisis Gugus Fungsi", type="primary"):
    
    st.subheader("📊 Hasil Analisis Sistem Pakar:")
    
    # LOGIKA IDENTIFIKASI (SISTEM PAKAR)
    
    # Kasus 1: Asam Karboksilat
    if uji_lakmus == "Berubah Menjadi Merah (Asam)":
        st.success("🎯 **Kesimpulan:** Sampel mengandung gugus **Asam Karboksilat (—COOH)**.")
        st.markdown("""
        **Penjelasan Analisis:**
        * Sifat asam yang mengubah lakmus biru menjadi merah mengindikasikan adanya pelepasan ion $H^+$.
        * Gugus fungsi ini memberikan sifat keasaman yang cukup kuat pada senyawa organik dibandingkan alkohol.
        """)
    
    # Kasus 2: Aldehid
    elif uji_schiff == "Positif (Muncul Warna Ungu Kemerahan)":
        st.success("🎯 **Kesimpulan:** Sampel mengandung gugus **Aldehid / Alkanal (—CHO)**.")
        st.markdown("""
        **Penjelasan Analisis:**
        * **Uji Schiff:** Reagen Schiff merupakan derivat fushsin yang warnanya dihilangkan oleh belerang dioksida. Ketika bereaksi dengan **Aldehid**, senyawa fushsin dibebaskan kembali sehingga memunculkan warna ungu kemerahan yang khas.
        """)
        
    # Kasus 3: Keton
    elif uji_bisulit == "Positif (Terbentuk Kristal/Endapan Putih)" and uji_schiff == "Tidak Bereaksi (Tetap Bening)":
        st.success("🎯 **Kesimpulan:** Sampel mengandung gugus **Keton / Alkanon (—CO—)**.")
        st.markdown("""
        **Penjelasan Analisis:**
        * **Uji Bisulfit:** Keton metil atau keton rantai pendek bereaksi adisi nukleofilik dengan $NaHSO_3$ jenuh membentuk senyawa adisi bisulfit berbentuk kristal putih. 
        * Hasil negatif pada Uji Schiff memastikan bahwa senyawa ini bukan aldehid, melainkan keton.
        """)
        
    # Kasus 4: Alkohol / Estera / Lainnya (Belum Spesifik)
    else:
        st.info("ℹ️ **Hasil:** Struktur belum dapat dipastikan secara spesifik.")
        st.write("Kemungkinan sampel adalah golongan **Alkohol** atau **Ester** netral. Lakukan uji lanjutan seperti uji Logam Natrium (untuk Alkohol) atau uji Hidrolisis Ester.")

else:
    st.warning("💡 Silakan pilih hasil pengamatan di atas, lalu klik tombol **Jalankan Analisis**.")
