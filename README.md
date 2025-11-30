# LIMEN: Web Fuzzer & LFI Detector (GUI)

**LIMEN** adalah alat sederhana berbasis Python untuk mendeteksi kerentanan *Local File Inclusion* (LFI) pada aplikasi web. Aplikasi ini dibangun menggunakan antarmuka grafis (GUI) Tkinter dan menerapkan konsep Pemrograman Berorientasi Objek (OOP) serta Struktur Data.

Project ini dibuat untuk Tugas Akhir Praktikum Pemrograman Dasar.

## 📂 Struktur Direktori

```text
LIMEN/
│
├── main.py              # Entry point (GUI & Main Logic)
├── modules/
│   ├── __init__.py
│   ├── scanner.py       # Logika OOP (Scanner Engine)
│   └── utils.py         # Struktur Data (Queue Implementation)
├── assets/
│   └── payloads.txt     # Database payload LFI
└── requirements.txt     # Dependency library
