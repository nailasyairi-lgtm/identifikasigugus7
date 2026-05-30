import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(page_title="Interactive Reagent Rack", page_icon="🧪", layout="centered")

# --- JUDUL ELEGAN ---
st.markdown("<h2 style='text-align: center; color: #0284C7; font-family: sans-serif;'>🧪 RAK REAGEN VIRTUAL</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B;'>Nyalakan sakelar reagen di bawah untuk menguji sampel misterius Anda!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- AREA MEJA KERJA LAB (INPUT SAKELAR) ---
st.markdown("### 🎛️ Panel Sakelar Reagen (On / Off)")

# Membuat 3 kolom rapi untuk sakelar reagen
col_reg1, col_reg2, col_reg3 = st.columns(3)

with col_reg1:
    st.markdown("**Uji Lakmus**")
    sakelar_lakmus = st.toggle("Celup Lakmus Biru", value=False)

with col_reg2:
    st.markdown("**Uji Schiff**")
    sakelar_schiff = st.toggle("Tetes Reagen Schiff", value=False)

with col_reg3:
    st.markdown("**Uji Bisulfit**")
    sakelar_bisulit = st.toggle("Tambah NaHSO3", value=False)

st.markdown("---")

# --- MEJA PENGAMATAN (OUTPUT) ---
st.markdown("### 🔍 Kondisi Fisik Tabung Reaksi")

# Logika penentuan warna tabung dan tebakan gugus fungsi
if sakelar_lakmus:
    # Jika lakmus dinyalakan (Asam Karboksilat)
    st.markdown("""
        <div style='background-color: #FEE2E2; border-left: 8px solid #EF4444; padding: 20px; border-radius: 8px;'>
            <h3 style='color: #991B1B; margin: 0;'>🔴 Tabung Bereaksi: WARNA MERAH</h3>
            <p style='color: #7F1D1D; margin-top: 10px; font-size: 16px;'>
                <b>Analisis Detektor:</b> Kertas lakmus biru langsung berubah menjadi merah! <br>
                🎯 Fix, sampel ini adalah golongan <b>ASAM KARBOKSILAT (—COOH)</b> karena memiliki ion H+ bebas.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif sakelar_schiff:
    # Jika schiff dinyalakan (Aldehid)
    st.markdown("""
        <div style='background-color: #FAE8FF; border-left: 8px solid #D946EF; padding: 20px; border-radius: 8px;'>
            <h3 style='color: #86198F; margin: 0;'>🟣 Tabung Bereaksi: WARNA UNGU KEMERAHAN</h3>
            <p style='color: #701A75; margin-top: 10px; font-size: 16px;'>
                <b>Analisis Detektor:</b> Reagen Schiff kembali ke warna asalnya akibat gugus karbonil bebas.<br>
                🎯 Fix, sampel ini adalah golongan <b>ALDEHID / ALKANAL (—CHO)</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

elif sakelar_bisulit:
    # Jika bisulfit dinyalakan (Keton)
    st.markdown("""
        <div style='background-color: #F8FAFC; border-left: 8px solid #64748B; padding: 20px; border-radius: 8px; border: 1px solid #CBD5E1;'>
            <h3 style='color: #334155; margin: 0;'>⚪ Tabung Bereaksi: TERBENTUK KRISTAL PUTIH</h3>
            <p style='color: #1E293B; margin-top: 10px; font-size: 16px;'>
                <b>Analisis Detektor:</b> Terjadi reaksi adisi nukleofilik yang menghasilkan garam sukar larut.<br>
                🎯 Fix, sampel ini adalah golongan <b>KETON / ALKANON (—CO—)</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

else:
    # Jika semua sakelar mati (Kondisi Awal)
    st.markdown("""
        <div style='background-color: #F0F9FF; border-left: 8px solid #0EA5E9; padding: 20px; border-radius: 8px;'>
            <h3 style='color: #075985; margin: 0;'>💧 Tabung Saat Ini: BENING & JERNIH</h3>
            <p style='color: #0C4A6E; margin-top: 10px;'>
                Belum ada reagen yang dimasukkan ke dalam sampel. Silakan klik/nyalakan salah satu <b>sakelar toggle</b> di atas untuk memulai reaksi kimia virtual!
            </p>
        </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("✨ Kelebihan versi ini: Menggunakan komponen UI murni, sangat ringan, dan bebas dari error crash.")
