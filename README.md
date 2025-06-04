<div align="center">
  <img src="https://img.shields.io/github/languages/count/keyvanarasteh/Project?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/keyvanarasteh/Project?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/keyvanarasteh/Project?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/keyvanarasteh/Project?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Network Scanner - Ağ Tarama Aracı
*Network Scanner Tool*

Python ile yazılmış kapsamlı bir ağ tarama aracı. Nmap ve Scapy kütüphanelerini kullanarak ağdaki cihazları tespit eder, canlılık kontrolü yapar, port taraması gerçekleştirir ve sonuçları CSV dosyasına kaydeder.

*A comprehensive network scanning tool written in Python. It detects devices on the network using Nmap and Scapy libraries, performs liveness checks, port scanning, and saves results to CSV files.*

---
## Features / *Özellikler*

- **Otomatik Ağ Geçidi Tespiti:** Varsayılan ağ geçidini otomatik tespit eder.  
  *Automatic Gateway Detection: Automatically detects the default network gateway.*
- **Canlılık Kontrolü:** Cihazların canlı olup olmadığını ICMP ping ile kontrol eder.  
  *Liveness Check: Checks if devices are alive using ICMP ping.*
- **Port Taraması:** Nmap ile hızlı OS tespiti ve port taraması yapar.  
  *Port Scanning: Performs fast OS detection and port scanning with Nmap.*
- **Hostname Çözümleme:** Cihazların hostname bilgilerini DNS ve reverse lookup ile alır.  
  *Hostname Resolution: Retrieves device hostname information via DNS and reverse lookup.*
- **Servis Tespiti:** Açık portları ve servis versiyonlarını listeler.  
  *Service Detection: Lists open ports and service versions.*
- **CSV Kayıt:** Tarama sonuçlarını `network_scan_results.csv` dosyasına kaydeder.  
  *CSV Export: Saves scan results to `network_scan_results.csv` file.*

---

## Team / *Ekip*

- *Ad Soyad: Ramazan Akçelik 
- *Ad Soyad: Yağız Veysel Demirel 
- *Ad Soyad: Mehmet Kerem Bıyık 


## Gereksinimler

- Python 3.6+
- [Scapy](https://scapy.net/)
- [python-nmap](https://pypi.org/project/python-nmap/)
- [netifaces](https://pypi.org/project/netifaces/)
- Nmap (sisteminde kurulu ve PATH'de veya `NMAP_PATH` ayarında doğru yol verilmiş olmalı)
- tqdm (İlerleme çubuğu için)

```bash
pip install scapy python-nmap netifaces tqdm
