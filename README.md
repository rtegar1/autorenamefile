# autorenamefile
"Automated file renamer with modern UI. Monitors directories for new scans and renames them to custom patterns (e.g., Prefix_1, Prefix_2) instantly using Python Watchdog."


# 📂 Auto-Rename Scanner (Sequential)

Aplikasi berbasis Python dengan antarmuka grafis (GUI) modern untuk memantau folder hasil scan secara otomatis dan memberikan penamaan file yang rapi menggunakan nomor urut.



## ✨ Fitur Utama
* **Real-time Monitoring**: Mendeteksi file baru secara instan di folder tujuan scan.
* **Sequential Naming**: Penamaan otomatis yang bersih (Contoh: `DOKUMEN_1.pdf`, `DOKUMEN_2.pdf`).
* **Modern UI**: Antarmuka gelap (Dark Mode) menggunakan `CustomTkinter`.
* **Safety Delay**: Memberikan jeda 1.5 detik agar file tidak terkunci saat diproses scanner.
* **Format Terintegrasi**: Mendukung file `.pdf`, `.jpg`, `.jpeg`, dan `.png`.

## 🛠️ Prasyarat (Requirements)
Jika Anda ingin menjalankan dari kode sumber:
* Python 3.x
* Library: `customtkinter`, `watchdog`

```bash
pip install customtkinter watchdog
