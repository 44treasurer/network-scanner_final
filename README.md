# Network Scanner - Ağ Tarama Aracı

Python ile yazılmış kapsamlı bir ağ tarama aracı. Nmap ve Scapy kütüphanelerini kullanarak ağdaki cihazları tespit eder, canlılık kontrolü yapar, port taraması gerçekleştirir ve sonuçları CSV dosyasına kaydeder.

---

## Özellikler

- Varsayılan ağ geçidini otomatik tespit eder.
- Belirtilen IP aralığında tarama yapabilir.
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
