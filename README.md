# 🏫 Sistem Dashboard Tata Usaha Sekolah (TU-Digital)

Sistem informasi berbasis web yang dirancang untuk memudahkan staf Tata Usaha dalam mengelola data SDM, kesiswaan, dan persuratan secara efisien dan elegan.
<img width="1293" height="716" alt="image" src="https://github.com/user-attachments/assets/d727424a-61c8-4fe1-b511-3a7167d9b93c" />
<img width="1901" height="922" alt="image" src="https://github.com/user-attachments/assets/ab723cf1-8048-4a71-92cc-3631e60ccda4" />


## 🚀 Fitur Utama
* **Sistem Login Keamanan:** Membatasi akses hanya untuk admin yang berwenang.
* **Visualisasi Data Interaktif:** Grafik tren persuratan dan komposisi guru menggunakan Plotly.
* **Manajemen Data Siswa:** * Unduh template Excel untuk standardisasi data.
    * Unggah (Import) data siswa massal langsung dari file Excel.
* **Antarmuka Elegan:** Header dan footer kustom dengan desain yang bersih dan responsif.

## 🛠️ Teknologi yang Digunakan
* **Bahasa:** Python 3.x
* **Framework:** [Streamlit](https://streamlit.io/)
* **Pengolahan Data:** Pandas
* **Visualisasi:** Plotly Express
* **Export/Import Excel:** XlsxWriter & Openpyxl

## 📋 Prasyarat
Sebelum menjalankan aplikasi, pastikan Anda telah menginstal Python di komputer Anda. Disarankan menggunakan lingkungan virtual (virtual environment).

## ⚙️ Instalasi

1. **Clone atau Download Repository ini.**
2. **Buka Terminal/Command Prompt** di folder proyek.
3. **Instal library yang diperlukan** dengan menjalankan perintah berikut:
   ```bash
   pip install streamlit pandas plotly openpyxl xlsxwriter
   ```
## 🏃 Cara Menjalankan Aplikasi
Jalankan perintah berikut di terminal:
``` bash
streamlit run app.py
```
Aplikasi akan secara otomatis terbuka di peramban (browser) default Anda di alamat http://localhost:8501.

## 🔐 Informasi Login Default
`Username`: admin\
`Password`: sekolah123

## 📂 Struktur File
`app.py`: File utama aplikasi Python/Streamlit.\
`README.md`: Dokumentasi petunjuk penggunaan (file ini).

© 2026 Dashboard Tata Usaha Digital - Dikembangkan untuk efisiensi sekolah.
