import os
import time
import threading
from datetime import datetime
import customtkinter as ctk
from tkinter import filedialog, messagebox
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# --- LOGIKA INTI (BACKEND) ---
class RenameHandler(FileSystemEventHandler):
    def __init__(self, prefix, app_instance):
        self.prefix = prefix
        self.app = app_instance

    def on_created(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_dir = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_name)[1].lower()

        # Filter format file
        if file_ext in ['.pdf', '.jpg', '.jpeg', '.png']:
            # Jeda agar file tidak 'locked' oleh sistem scanner
            time.sleep(1.5) 
            
            # --- LOGIKA NOMOR URUT (TANPA TIMESTAMP) ---
            counter = 1
            while True:
                # Menghasilkan nama: Prefix_1.pdf, Prefix_2.pdf, dst.
                new_filename = f"{self.prefix}_{counter}{file_ext}"
                new_path = os.path.join(file_dir, new_filename)
                
                # Cek jika nama file sudah ada, naikkan nomor urut
                if not os.path.exists(new_path):
                    break
                counter += 1
            
            try:
                os.rename(file_path, new_path)
                self.app.log_message(f"BERHASIL: {file_name} -> {new_filename}")
            except Exception as e:
                self.app.log_message(f"ERROR: {str(e)}")

# --- ANTARMUKA PENGGUNA (GUI) ---
class ScanRenamerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Auto Rename Scan (Sequential)")
        self.geometry("550x450")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.observer = None
        self.is_running = False

        # UI Layout
        self.label_title = ctk.CTkLabel(self, text="Scanner File Watcher", font=("Arial", 22, "bold"))
        self.label_title.pack(pady=(20, 10))

        # Pilih Folder
        self.frame_folder = ctk.CTkFrame(self)
        self.frame_folder.pack(pady=10, padx=20, fill="x")

        self.folder_path = ctk.StringVar(value="Belum ada folder terpilih...")
        self.label_folder = ctk.CTkLabel(self.frame_folder, textvariable=self.folder_path, wraplength=400)
        self.label_folder.pack(pady=5)

        self.btn_browse = ctk.CTkButton(self.frame_folder, text="Pilih Folder Scan", command=self.browse_folder)
        self.btn_browse.pack(pady=10)

        # Input Prefix
        self.label_prefix = ctk.CTkLabel(self, text="Nama File Utama (Tanpa Angka):")
        self.label_prefix.pack()
        self.entry_prefix = ctk.CTkEntry(self, placeholder_text="Contoh: LAPORAN_BULANAN", width=300)
        self.entry_prefix.pack(pady=(0, 20))

        # Tombol Start/Stop
        self.btn_action = ctk.CTkButton(self, text="Mulai Pantau Folder", 
                                        fg_color="#2ecc71", hover_color="#27ae60",
                                        font=("Arial", 14, "bold"),
                                        command=self.toggle_monitoring)
        self.btn_action.pack(pady=10)

        # Log Aktivitas
        self.log_box = ctk.CTkTextbox(self, width=500, height=120, font=("Consolas", 12))
        self.log_box.pack(pady=10, padx=20)
        self.log_message("Sistem siap. Gunakan nomor urut otomatis.")

    def browse_folder(self):
        path = filedialog.askdirectory()
        if path:
            self.folder_path.set(path)
            self.log_message(f"Folder diatur ke: {path}")

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_box.insert("end", f"[{timestamp}] {message}\n")
        self.log_box.see("end")

    def toggle_monitoring(self):
        if not self.is_running:
            target_folder = self.folder_path.get()
            prefix = self.entry_prefix.get().strip()

            if not os.path.exists(target_folder) or target_folder == "Belum ada folder terpilih...":
                messagebox.showwarning("Peringatan", "Silakan pilih folder scan lebih dahulu!")
                return
            
            prefix = prefix if prefix else "SCAN"
            self.start_monitoring(target_folder, prefix)
        else:
            self.stop_monitoring()

    def start_monitoring(self, folder, prefix):
        self.event_handler = RenameHandler(prefix, self)
        self.observer = Observer()
        self.observer.schedule(self.event_handler, folder, recursive=False)
        self.observer.start()
        
        self.is_running = True
        self.btn_action.configure(text="Berhenti Pantau", fg_color="#e74c3c", hover_color="#c0392b")
        self.entry_prefix.configure(state="disabled")
        self.log_message(f"MEMANTAU: {folder} (Prefix: {prefix})")

    def stop_monitoring(self):
        if self.observer:
            self.observer.stop()
            self.observer.join()
        
        self.is_running = False
        self.btn_action.configure(text="Mulai Pantau Folder", fg_color="#2ecc71", hover_color="#27ae60")
        self.entry_prefix.configure(state="normal")
        self.log_message("Monitoring dihentikan.")

if __name__ == "__main__":
    app = ScanRenamerApp()
    app.mainloop()