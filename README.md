 Fitur Utama
Ping Sweep (ICMP Echo Request)
Melakukan pemindaian jaringan untuk mendeteksi host yang aktif pada subnet tertentu menggunakan protokol ICMP. Hasilnya adalah daftar alamat IP yang merespons ping.

TCP Port Scan (SYN Scan)
Melakukan pemindaian port TCP untuk mengecek port terbuka pada sebuah host dengan menggunakan metode TCP SYN (half-open scan), mirip dengan teknik yang digunakan nmap.

🚀 Cara Menjalankan
Aktifkan virtual environment (opsional tapi disarankan):

bash
Copy
Edit
.venv\Scripts\activate
Jalankan program:

bash
Copy
Edit
python scanning.py
Ikuti petunjuk menu interaktif.

⚠️ Hak Akses
Program ini memerlukan akses root/admin untuk mengirimkan paket ICMP dan TCP mentah. Jalankan dengan Run as Administrator (Windows) atau sudo (Linux/Mac) jika diperlukan.

🛠️ Dependensi
scapy

ipaddress

concurrent.futures (builtin)

socket, subprocess, datetime (builtin)

Instalasi dependensi:

bash
Copy
Edit
pip install scapy