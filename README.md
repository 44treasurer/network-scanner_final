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

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                       |
|-------------------------|-----------------------------------------|------------------------------------------------|
|     Nmap                |   researchs/nmap.md                     | Comprehensive guide to Nmap network scanning techniques. / Nmap ağ tarama 
|                         |                                         | tekniklerinin kapsamlı rehberi.  
|                         |                                         |
|   OpenAI                | researchs/openai.md                     |Research on AI integration for automated network analysis. / Otomatik ağ   
|                         |                                         |analizi için AI entegrasyonu araştırması.
|                         |                                         |
|   Claude                |researchs/claude.md                      | Exploring Claude AI for intelligent security reporting. / Akıllı güvenlik |                         |                                         | raporlaması için Claude AI keşfi.                     
|                         |                                         |
|  Gemini                 | researchs/gemini.md                     |Gemini AI applications in network vulnerability assessment. / Ağ güvenlik                                                                      |açığı değerlendirmesinde Gemini AI uygulamaları.

---

## Installation / *Kurulum*



1. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install System Dependencies / *Sistem Bağımlılıklarını Yükleyin***:
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get update
   sudo apt-get install nmap python3-dev python3-pip
   ```
   
   **macOS:**
   ```bash
   brew install nmap
   ```
   
   **Windows:**
   - Download and install Nmap from: https://nmap.org/download.html
   - Make sure Python is installed from: https://python.org

4. **Install Python Dependencies / *Python Bağımlılıklarını Yükleyin***:  
   ```bash
   pip install python-nmap netifaces tqdm
   ```
   
   **Required Libraries / *Gerekli Kütüphaneler***:
   - `python-nmap`: Nmap Python wrapper
   - `netifaces`: Network interface information
   - `tqdm`: Progress bar for terminal
   - `subprocess`: Built-in Python module
   - `socket`: Built-in Python module
   - `time`: Built-in Python module
   - `csv`: Built-in Python module
   - `argparse`: Built-in Python module

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python network_scanner.py --target 192.168.1.0/24 --output scan_results.csv
```

**Steps**:  
1. Prepare network target (*specify IP range or single IP*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*results will be saved to CSV file*).  

*Adımlar*:  
1. Ağ hedefini hazırlayın (*IP aralığı veya tek IP belirtin*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçlar CSV dosyasına kaydedilecek*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/YOUR_REPO.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  


---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Nmap Project: For providing the powerful network scanning engine.  
- Python Community: For excellent networking libraries.  
- Open Source Contributors: For continuous improvements.  

*Teşekkürler: Güçlü ağ tarama motoru ve mükemmel ağ kütüphaneleri için.*

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
