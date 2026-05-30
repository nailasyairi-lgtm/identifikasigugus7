import streamlit as st

# Konfigurasi Halaman Web
st.set_page_config(page_title="Chemical RPG Game", page_icon="🎮", layout="centered")

# --- INISIALISASI DATA GAME (Penyimpanan Sementara) ---
# Menggunakan session_state agar nilai tidak ter-reset saat tombol diklik
if 'nyawa' not in st.session_state:
    st.session_state.nyawa = 3
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'status_game' not in st.session_state:
    st.session_state.status_game = "BERMAIN" # Pilihan: BERMAIN, MENANG, GAME_OVER

# --- FUNGSI UNTUK RESET GAME ---
def reset_game():
    st.session_state.nyawa = 3
    st.session_state.skor = 0
    st.session_state.status_game = "BERMAIN"

# --- TAMPILAN HEADER GAME ---
st.markdown("<h1 style='text-align: center; color: #4F46E5;'>🎮 LAB ADVENTURE: Misteri Gugus Fungsi</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'>Misi: Tebak isi botol misterius di laboratorium sebelum energi Anda habis!</p>", unsafe_allow_html=True)
st.markdown("---")

# --- PANEL STATUS PLAYER (Scoreboard Berwarna) ---
col_stat1, col_stat2 = st.columns(2)
with col_stat1:
    st.markdown(f"### ❤️ Energi: {'⭐' * st.session_state.nyawa if st.session_state.nyawa > 0 else '❌ Lelah'}")
with col_stat2:
    st.markdown(f"### 🏆 Skor: `{st.session_state.skor} Poin`")

st.markdown("---")

# ==========================================
# JALUR CERITA & LOGIKA GAME
# ==========================================

# STATUS 1: JIKA GAME OVER
if st.session_state.status_game == "GAME_OVER":
    st.error("💥 **GAME OVER!** Anda salah mencampurkan bahan kimia berbahaya dan laboratorium meledak!")
    st.write("Jangan menyerah, seorang analis hebat belajar dari kegagalan.")
    if st.button("🔄 Ulangi Misi (Reset Game)", type="primary"):
        reset_game()
        st.rerun()

# STATUS 2: JIKA MENANG
elif st.session_state.status_game == "MENANG":
    st.balloons() # Efek selebrasi balon di layar
    st.success(f"🎉 **SELAMAT!** Anda berhasil menyelesaikan teka-teki laboratorium dengan skor akhir {st.session_state.skor}!")
    st.write("👨‍🔬 Dosen pembimbing bangga pada Anda. Anda berhak mendapatkan gelar *Master of Organic Chemistry*!")
    if st.button("🎮 Main Lagi", type="primary"):
        reset_game()
        st.rerun()

# STATUS 3: SEDANG BERMAIN
else:
    st.markdown("### 🥼 Situasi Ruangan:")
    st.info("Anda menemukan botol kaca buram berisi cairan bening berbau tajam. Di meja tersedia 3 reagen uji.")
    st.write(" Silakan pilih **satu reagen** yang menurut Anda paling aman dan tepat untuk menguji sampel:")

    # Tombol Pilihan Action/Reagen
         pilihan_aksi = st.radio(
        "Pilih tindakan Anda:",
        [
            "👉 Uji dengan Kertas Lakmus Biru (Cek Sifat Asam)",
            "👉 Teteskan Reagen Schiff (Cek Gugus Aldehid)",
            "👉 Tambahkan Larutan Perak Nitrat / Tollens (Uji Cermin Perak)"
        ],
        index=None, # Membikin pilihan kosong di awal
        placeholder="Pilih opsi untuk melangkah..."
    )

    st.markdown("---")

    # Tombol untuk Submit Jawaban / Melangkah
    if pilihan_aksi:
        st.markdown("### 🎬 Hasil Tindakan Anda:")
        
        # SAKLAR LOGIKA JAWABAN GAME
        
        # Opsi 1: Jawaban Salah/Zonk (Uji Lakmus)
        if "Kertas Lakmus Biru" in pilihan_aksi:
            st.markdown("""
                <div style='background-color: #FEF2F2; border-left: 5px solid #EF4444; padding: 15px; border-radius: 5px;'>
                    <p style='color: #991B1B; margin: 0;'>
                        <b>Hasil:</b> Kertas lakmus tetap berwarna biru (Senyawa Netral). <br>
                        ⚠️ Anda tidak mendapatkan petunjuk apa pun dan membuang-buang waktu laboratorium!
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Mengurangi Nyawa
            if st.button("Lanjutkan Langkah ➡️"):
                st.session_state.nyawa -= 1
                if st.session_state.nyawa <= 0:
                    st.session_state.status_game = "GAME_OVER"
                st.rerun()

        # Opsi 2: Jawaban Setengah Benar (Uji Schiff)
        elif "Reagen Schiff" in pilihan_aksi:
            st.markdown("""
                <div style='background-color: #FFFBEB; border-left: 5px solid #F59E0B; padding: 15px; border-radius: 5px;'>
                    <p style='color: #92400E; margin: 0;'>
                        <b>Hasil:</b> Larutan tetap bening, tidak berubah menjadi ungu kemerahan. <br>
                        💡 <b>Petunjuk Didapat:</b> Fix! Sampel ini 100% <u>BUKAN Aldehid</u>. Berarti kemungkinan besar adalah Keton!
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Menambah Skor Kecil
            if st.button("Lanjutkan Langkah ➡️"):
                st.session_state.skor += 50
                st.rerun()

        # Opsi 3: Jawaban Benar / Kunci Kemenangan (Uji Tollens)
        elif "Perak Nitrat" in pilihan_aksi:
            st.markdown("""
                <div style='background-color: #ECFDF5; border-left: 5px solid #10B981; padding: 15px; border-radius: 5px;'>
                    <p style='color: #065F46; margin: 0;'>
                        <b>Hasil:</b> Dinding tabung reaksi tiba-tiba dilapisi lapisan perak mengkilap seperti cermin! <br>
                        🎯 <b>ANALISIS SEMPURNA:</b> Reaksi cermin perak positif membuktikan sampel adalah <b>ALDEHID</b>! Misi berhasil diselesaikan!
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Menang Game
            if st.button("Klaim Kemenangan 🏆"):
                st.session_state.skor += 200
                st.session_state.status_game = "MENANG"
                st.rerun()
