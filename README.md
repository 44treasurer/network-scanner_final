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

## Özellikler

- Varsayılan ağ geçidini otomatik tespit eder.
- Cihazların canlı olup olmadığını ICMP ping ile kontrol eder.
- Nmap ile hızlı OS tespiti ve port taraması yapar.
- Cihazların hostname bilgilerini DNS ve reverse lookup ile alır.
- Açık portları ve servis versiyonlarını listeler.
- Tarama sonuçlarını `network_scan_results.csv` dosyasına kaydeder.


---

## Gereksinimler

- Python 3.6+
- [Scapy](https://scapy.net/)
- [python-nmap](https://pypi.org/project/python-nmap/)
- [netifaces](https://pypi.org/project/netifaces/)
- Nmap (sisteminde kurulu ve PATH'de veya `NMAP_PATH` ayarında doğru yol verilmiş olmalı)
- tqdm (İlerleme çubuğu için)

```bash
pip install scapy python-nmap netifaces tqdm
