import socket
import subprocess
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP
import concurrent.futures
from datetime import datetime

def ping_sweep(network):
    active_host = []
    try:
        network = ipaddress.ip_network(network, strict=False)
    except ValueError as e:
        print(f"Error: {e}")
        return active_host
    
    print(f"\nMemulai ping sweep untuk jaringan {network}...")

    def ping(ip):
        try:
            packet = IP(dst=str(ip))/ICMP()
            response = sr1(packet, timeout=1, verbose=0)
            if response is not None:
                print(f"Host aktif ditemukan: {ip}")
                active_host.append(str(ip))
                return ip
        except Exception as e:
            pass
        return None
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(ping, ip) for ip in network.hosts()]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    return active_host

def tcp_port_scan(host, ports):
    open_ports = []
    print(f"\nMemulai TCP scan pada {host}")

    def scan_port(port):
        try:
            packet = IP(dst=host)/TCP(dport=port, flags="S")
            response = sr1(packet, timeout=1, verbose=0)

            if response is not None and response.haslayer(TCP):
                if response.getlayer(TCP).flags == 0x12:  # SYN-ACK
                    sr1(IP(dst=host)/TCP(dport=port, flags="R"), timeout=1, verbose=0)  # RST
                    open_ports.append(port)
                    print(f"Port {port} terbuka")
        except Exception as e:
            pass
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, port) for port in ports]
        for future in concurrent.futures.as_completed(futures):
            future.result()
    
    return open_ports

def main():
    while True:
        print("\nMenu:")
        print("1. Ping Sweep (ICMP Echo Request)")
        print("2. TCP Port Scan (SYN Scan)")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1-3): ")
        
        if choice == "1":
            network = input("Masukkan jaringan : ")
            start_time = datetime.now()
            active_hosts = ping_sweep(network)
            end_time = datetime.now()
            
            print("\nHasil Ping Sweep:")
            if active_hosts:
                print("Host aktif:")
                for host in active_hosts:
                    print(f"- {host}")
            else:
                print("Tidak ada host aktif yang ditemukan.")
            
            print(f"\nWaktu eksekusi: {end_time - start_time}")
            
        elif choice == "2":
            host = input("Masukkan alamat IP target: ")
            port_input = input("Masukkan port/range port (contoh: 80 atau 1-100): ")
            
            try:
                if "-" in port_input:
                    start_port, end_port = map(int, port_input.split("-"))
                    ports = range(start_port, end_port + 1)
                else:
                    ports = [int(port_input)]
            except ValueError:
                print("Format port tidak valid!")
                continue
            
            start_time = datetime.now()
            open_ports = tcp_port_scan(host, ports)
            end_time = datetime.now()
            
            print("\nHasil TCP Port Scan:")
            if open_ports:
                print("Port terbuka:")
                for port in sorted(open_ports):
                    print(f"- {port}")
            else:
                print("Tidak ada port terbuka yang ditemukan.")
            
            print(f"\nWaktu eksekusi: {end_time - start_time}")
            
        elif choice == "3":
            print("Keluar dari program...")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    try:
        if not (hasattr(socket, 'AF_PACKET') or (subprocess.run(["whoami"], capture_output=True, text=True).stdout.strip() != "root")):
            print("Warning: Program ini memerlukan hak akses root/admin untuk berfungsi dengan baik.")
    except:
        pass
    
    main()