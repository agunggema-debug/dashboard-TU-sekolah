import streamlit as st
import pandas as pd
import plotly.express as px
import io
from datetime import datetime

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Sistem TU Sekolah", layout="wide")

# --- CSS CUSTOM ---
st.markdown("""
    <style>
    .header-style { padding: 20px; background-color: #1E3A8A; color: white; border-radius: 10px; text-align: center; margin-bottom: 25px; }
    .footer-style { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #f1f1f1; color: #555; text-align: center; padding: 10px; border-top: 1px solid #ddd; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1E3A8A; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI LOGIN ---
def login():
    st.markdown("<h2 style='text-align: center;'>🔐 Login Admin TU</h2>", unsafe_allow_html=True)
    with st.container():
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if st.button("Masuk"):
                if username == "admin" and password == "sekolah123":
                    st.session_state['logged_in'] = True
                    st.rerun()
                else:
                    st.error("Username atau password salah!")

# --- CEK STATUS LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    login()
else:

# --- KONFIGURASI HALAMAN ---
    st.set_page_config(page_title="Dashboard Tata Usaha Sekolah", layout="wide")

    # --- CSS CUSTOM UNTUK TAMPILAN ELEGAN ---
    st.markdown("""
        <style>
        .main {
            background-color: #f5f7f9;
        }
        .header-style {
            padding: 20px;
            background-color: #1E3A8A;
            color: white;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 25px;
        }
        .footer-style {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #555;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            border-top: 1px solid #ddd;
        }
        </style>
        """, unsafe_allow_html=True)

    # --- HEADER ---
    st.markdown("""
        <div class="header-style">
            <h1>Sistem Informasi Tata Usaha Sekolah</h1>
            <p>Manajemen Data Terpusat & Monitoring Real-time</p>
        </div>
        """, unsafe_allow_html=True)

    # --- SIDEBAR NAVIGASI ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/2602/2602414.png", width=100)
        st.title("Menu Utama")
        menu = st.radio("Pilih Layanan:", ["Beranda", "Data Guru & Staf", "Kesiswaan", "Persuratan"])
        st.info(f"Tanggal: {datetime.now().strftime('%d %B %Y')}")

    # --- DATA DUMMY ---
    data_guru = pd.DataFrame({
        'Kategori': ['Guru Tetap', 'Guru Honorer', 'Staf TU', 'Keamanan'],
        'Jumlah': [45, 12, 8, 4]
    })

    data_surat = pd.DataFrame({
        'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei'],
        'Masuk': [20, 35, 30, 45, 40],
        'Keluar': [15, 25, 20, 30, 35]
    })

    # --- KONTEN UTAMA ---
    if menu == "Beranda":
        # Ringkasan Statistik dalam Kolom
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Siswa", "1,240", "12%")
        col2.metric("Total Guru", "57", "2%")
        col3.metric("Surat Masuk", "170")
        col4.metric("Kehadiran Staf", "98%")

        st.markdown("---")

        col_left, col_right = st.columns(2)

        with col_left:
            st.subheader("Komposisi SDM Sekolah")
            fig1 = px.pie(data_guru, values='Jumlah', names='Kategori', hole=0.4,
                        color_discrete_sequence=px.colors.sequential.RdBu)
            st.plotly_chart(fig1, use_container_width=True)

        with col_right:
            st.subheader("Tren Persuratan (2025)")
            fig2 = px.line(data_surat, x='Bulan', y=['Masuk', 'Keluar'], markers=True)
            st.plotly_chart(fig2, use_container_width=True)

    elif menu == "Data Guru & Staf":
        st.subheader("Manajemen Data Pendidik")
        st.table(data_guru)
        st.button("Tambah Data Guru Baru")

    elif menu == "Kesiswaan":
        st.subheader("Impor Data Siswa Baru")
        st.info("Unggah file Excel (.xlsx) yang berisi kolom: Nama, Kelas, NISN, dan Alamat.")

        # --- LOGIKA DOWNLOAD TEMPLATE ---
        # Membuat data dummy untuk template
        template_data = pd.DataFrame({
            'Nama': ['Budi Santoso', 'Siti Aminah'],
            'Kelas': ['10-A', '10-B'],
            'NISN': ['0012345678', '0087654321'],
            'Alamat': ['Jl. Merdeka No. 1', 'Jl. Sudirman No. 10']
        })

        # Fungsi untuk mengonversi dataframe ke Excel
        def to_excel(df):
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            return output.getvalue()    
        template_xlsx = to_excel(template_data)

        # Tombol Download Template
        st.download_button(
            label="📥 Download Template Excel Siswa",
            data=template_xlsx,
            file_name='template_siswa_baru.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )

        st.markdown("---") # Garis pemisah
        
        # Komponen Upload File
        uploaded_file = st.file_uploader("Pilih file Excel", type=["xlsx", "xls"])

        if uploaded_file is not None:
            try:
                # Membaca file excel
                df_siswa = pd.read_excel(uploaded_file)
                
                # Menampilkan Statistik Sederhana dari File
                st.success("File berhasil diunggah!")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Preview Data:**")
                    st.dataframe(df_siswa.head(), use_container_width=True)
                
                with col2:
                    st.write("**Ringkasan Data:**")
                    st.write(f"- Total Baris: {df_siswa.shape[0]}")
                    st.write(f"- Total Kolom: {df_siswa.shape[1]}")
                    
                    # Contoh Visualisasi Sederhana dari Data yang diunggah
                    if 'Kelas' in df_siswa.columns:
                        st.write("**Distribusi per Kelas:**")
                        kelas_counts = df_siswa['Kelas'].value_counts()
                        st.bar_chart(kelas_counts)

                # Tombol Konfirmasi Simpan
                if st.button("Simpan ke Database"):
                    # Di sini Anda bisa menambahkan logika koneksi ke database SQL
                    st.balloons()
                    st.success("Data telah berhasil diintegrasikan ke sistem utama!")

            except Exception as e:
                st.error(f"Terjadi kesalahan saat membaca file: {e}")
        else:
            st.write("Silakan unggah file untuk melihat pratinjau data.")

    else:
        st.warning("Halaman ini sedang dalam pengembangan.")

    # --- FOOTER ---
    st.markdown("""
        <div class="footer-style">
            © 2026 Dashboard TU Digital | SMA Negeri Unggul Jaya | Hubungi Agung Gema: 0813-9892-0798
        </div>
        """, unsafe_allow_html=True)