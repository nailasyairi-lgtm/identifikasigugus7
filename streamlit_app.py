import streamlit as st
import matplotlib.pyplot as plt

# Konfigurasi Halaman Web
st.set_page_config(page_title="Chemical Detective Lab", page_icon="🕵️‍♂️", layout="centered")

# --- STYLE CSS UNTUK MENAMPILKAN VIBE LABORATORIUM ---
st.markdown("""
    <style>
    .reportview-container { background: #f5f7f8; }
    .stRadio > div { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 1px 1px 5px rgba(0,0,0,0.05); }
    h1 { font-family: 'Courier New', Courier, monospace; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER GAME / DETEKTIF ---
st.markdown("<h1 style='text-align: center; color: #0F172A;'>🕵️‍♂️ DETEKTIF KIMIA: Misi Kode Sampel X</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>Sebuah sampel misterius tanpa label ditemukan di meja lab. Gunakan reagen untuk mengungkap identitasnya!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- INPUT LOGBOOK ANALIS ---
col_info1, col_info2 = st.columns(2)
with col_info1:
    nama_analis = st.text_input("✍️ Nama Analis / Detektif:", "Analis AKA")
with col_info2:
    kode_sampel = st.text_input("🏷️ Kode Botol Sampel:", "SAMPEL-007")

st.write("")

# --- PROSEDUR PENGUJIAN (INPUT) ---
st.markdown("### 🧪 Langkah Pengujian Reagen")

# Menggunakan expander agar UI terlihat rapi seperti tahapan SOP Lab
with st.expander("🔬 LANGKAH 1: Uji Lakmus (Sifat Asam/Basa)", expanded=True):
    uji_lakmus = st.radio(
        "Celupkan kertas lakmus biru ke dalam sampel, apa yang terjadi?",
        ["Warna tetap Biru (Netral/Basa)", "Warna berubah menjadi Merah (Asam)"]
    )

with st.expander("🔬 LANGKAH 2: Uji Reagen Schiff (Spesifik Aldehid)", expanded=True):
    uji_schiff = st.radio(
        "Teteskan 3 tetes reagen Schiff ke dalam tabung reaksi:",
        ["Larutan tetap bening tak berwarna", "Larutan berubah menjadi ungu kemerahan / fushsin"]
    )

with st.expander("🔬 LANGKAH 3: Uji Natrium Bisulfit (Gugus Karbonil)", expanded=True):
    uji_bisulit = st.radio(
        "Tambahkan larutan NaHSO3 jenuh ke dalam sampel:",
        ["Tidak ada gejala reaksi (Tetap jernih)", "Terbentuk endapan kristal putih di dasar tabung"]
    )

st.markdown("---")

# --- LOGIKA ANALISIS & VISUALISASI STRUKTUR ---
st.markdown("<h3 style='text-align: center; color: #0F172A;'>📂 Laporan Hasil Investigasi</h3>", unsafe_allow_html=True)

# Fungsi untuk menggambar struktur molekul buatan (Simpel & Unik menggunakan Matplotlib)
def gambar_struktur(gugus):
    fig, ax = plt.subplots(figsize=(3, 2))
    ax.axis('off')
    if gugus == "Asam Karboksilat":
        # Menggambar R-C(=O)-OH
        ax.text(0.1, 0.5, "R", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.3, 0.5, "— C", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.5, 0.8, "═ O", fontsize=20, weight='bold', color='#EF4444') # O ganda di atas
        ax.text(0.6, 0.2, "— OH", fontsize=20, weight='bold', color='#0EA5E9')
    elif gugus == "Aldehid":
        # Menggambar R-C(=O)-H
        ax.text(0.1, 0.5, "R", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.3, 0.5, "— C", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.5, 0.8, "═ O", fontsize=20, weight='bold', color='#EF4444')
        ax.text(0.6, 0.2, "— H", fontsize=20, weight='bold', color='#10B981')
    elif gugus == "Keton":
        # Menggambar R-C(=O)-R'
        ax.text(0.1, 0.5, "R", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.3, 0.5, "— C", fontsize=20, weight='bold', color='#1E293B')
        ax.text(0.5, 0.8, "═ O", fontsize=20, weight='bold', color='#EF4444')
        ax.text(0.6, 0.2, "— R'", fontsize=20, weight='bold', color='#F59E0B')
    return fig

# Evaluasi Hasil Game Detektif
status_ditemukan = False
gugus_nama = ""

if "Warna berubah menjadi Merah" in uji_lakmus:
    gugus_nama = "Asam Karboksilat"
    status_ditemukan = True
    st.error(f"### 🎉 MISI BERHASIL: {kode_sampel} adalah ASAM KARBOKSILAT!")
    
elif "Larutan berubah menjadi ungu" in uji_schiff:
    gugus_nama = "Aldehid"
    status_ditemukan = True
    st.success(f"### 🎉 MISI BERHASIL: {kode_sampel} adalah ALDEHID (ALKANAL)!")

elif "Terbentuk endapan kristal" in uji_bisulit and "Larutan tetap bening" in uji_schiff:
    gugus_nama = "Keton"
    status_ditemukan = True
    st.warning(f"### 🎉 MISI BERHASIL: {kode_sampel} adalah KETON (ALKANON)!")

# Tampilkan Informasi Spesifikasi Unik jika Berhasil Ditebak
if status_ditemukan:
    st.balloons() # Efek selebrasi balon di layar!
    
    col_has1, col_has2 = st.columns([1, 1])
    with col_has1:
        st.write("**Sketsa Rumus Struktur Gugus:**")
        st.pyplot(gambar_struktur(gugus_nama))
    with col_has2:
        st.markdown(f"""
        **Sertifikat Analisis Digital:**
        * 🕵️‍♂️ **Pemeriksa:** {nama_analis}
        * 🧪 **Gugus Utama:** `{gugus_nama}`
        * 📈 **Tingkat Akurasi:** 99.8% (Sistem Pakar)
        """)
        st.info("💡 Struktur di samping adalah representasi ikatan karbonil dan fungsional zat sampel kamu.")
else:
    st.markdown(
        """
        <div style='background-color: #1E293B; padding: 20px; border-radius: 10px; text-align: center;'>
            <h4 style='color: #FFFFFF; margin-top:0;'>🕵️‍♂️ Detektif Sedang Berpikir...</h4>
            <p style='color: #94A3B8; margin-bottom:0;'>
                Kombinasi reagen saat ini condong ke senyawa Netral (seperti <b>Alkohol</b> atau <b>Ester</b>). <br>
                Cobalah ubah salah satu opsi reagen di atas untuk melihat perubahan zat!
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
