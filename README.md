#  Network Scanner - Ping Sweep & TCP SYN Scanner

This is a Final Project for the **Computer Networks** course, featuring a simple Python-based network scanning tool. The program offers two main features: **Ping Sweep (ICMP Echo Request)** and **TCP SYN Port Scanning**, presented through an interactive terminal-based menu.

---

##  Features

### 1. Ping Sweep (ICMP)
- Scans all hosts within a given subnet (e.g., `192.168.1.0/24`)
- Sends ICMP Echo Requests to detect active hosts
- Displays a list of reachable (alive) IPs

### 2. TCP SYN Port Scan
- Scans for open TCP ports on a target IP using the TCP SYN (half-open) scanning technique
- Supports scanning a single port or a range (e.g., `80` or `1-100`)

---
##  Installation & Setup
<pre><code>pip install scapy</code></pre>

----
## Running the Program
<pre><code>python net_scanning.py</code></pre>

-----
## output project
![output](picture/output0.pgn)
!(picture/output1.pgn)

#### Febriyanti Rahayu

