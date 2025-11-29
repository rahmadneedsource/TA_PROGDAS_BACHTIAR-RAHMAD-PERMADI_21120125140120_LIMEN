import tkinter as tk
from tkinter import scrolledtext, messagebox
import os

# Import modul buatan sendiri
from modules.scanner import LFIScanner
from modules.utils import LogQueue

class LimenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LIMEN - Web Fuzzer & LFI Detector")
        self.root.geometry("600x450")
        
        # Inisialisasi Queue
        self.log_queue = LogQueue()

        # --- GUI COMPONENTS (Modul 8) ---
        
        # Label & Input URL
        tk.Label(root, text="Target URL (ex: http://testphp.vulnweb.com/showimage.php?file=)").pack(pady=5)
        self.url_entry = tk.Entry(root, width=60)
        self.url_entry.pack(pady=5)

        # Tombol Scan
        self.scan_btn = tk.Button(root, text="Mulai Scanning", command=self.run_scan, bg="#ff4d4d", fg="white")
        self.scan_btn.pack(pady=10)

        # Output Area
        tk.Label(root, text="Log Aktivitas:").pack()
        self.log_area = scrolledtext.ScrolledText(root, width=70, height=15)
        self.log_area.pack(pady=10)

        # Status Bar
        self.status_label = tk.Label(root, text="Siap.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def load_payloads(self):
        # Membaca file payloads
        payloads = []
        path = "assets/payloads.txt"
        if os.path.exists(path):
            with open(path, "r") as f:
                # List Comprehension (Modul 1 & 2)
                payloads = [line.strip() for line in f.readlines()]
        else:
            messagebox.showerror("Error", "File assets/payloads.txt tidak ditemukan!")
        return payloads

    def run_scan(self):
        target = self.url_entry.get()
        
        # Validasi Input (Modul 3)
        if not target.startswith("http"):
            messagebox.showwarning("Peringatan", "URL harus diawali http:// atau https://")
            return

        self.log_area.delete(1.0, tk.END)
        self.status_label.config(text="Sedang memindai...")
        self.root.update() # Agar GUI tidak freeze sesaat

        # Load payload
        payload_list = self.load_payloads()
        
        if not payload_list:
            return

        # Instansiasi Objek (Modul 5)
        scanner = LFIScanner(target, payload_list)
        
        # Jalankan Scan
        scanner.scan(self.log_queue)

        # Tampilkan hasil dari Queue (Modul 7)
        while not self.log_queue.is_empty():
            log = self.log_queue.dequeue()
            self.log_area.insert(tk.END, log + "\n")
            # Auto scroll ke bawah
            self.log_area.see(tk.END)

        self.status_label.config(text="Scanning Selesai.")
        messagebox.showinfo("Selesai", "Proses scanning telah selesai.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LimenApp(root)
    root.mainloop()