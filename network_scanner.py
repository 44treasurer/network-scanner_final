#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scapy.all as scapy
scapy.conf.verb = 0  # Scapy verbose çıktı kapatma

import nmap
import subprocess
import netifaces
import socket
import time
import csv
import argparse
from tqdm import tqdm

# Nmap'in tam yolu (Kendi sistemine göre değiştir!)
NMAP_PATH = r"C:\Program Files (x86)\Nmap\nmap.exe"

def get_default_gateway_ip():
    try:
        gws = netifaces.gateways()
        return gws['default'][netifaces.AF_INET][0]
    except Exception as e:
        print(f"Varsayılan ağ geçidi bulunamadı: {e}")
        return None

def get_network_range(gateway_ip):
    try:
        ip_parts = gateway_ip.split('.')
        network_prefix = '.'.join(ip_parts[:3])
        network_range = f"{network_prefix}.0/24"
        return network_range
    except Exception as e:
        print(f"Ağ aralığı belirlenemedi: {e}")
        return None

def get_hostname(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        pass
    try:
        output = subprocess.check_output(
            ['nslookup', ip_address],
            stderr=subprocess.DEVNULL,  # Hata mesajlarını gizle
            timeout=3
        ).decode('utf-8')
        if 'name =' in output:
            return output.split('name =')[1].split('\n')[0].strip()
    except Exception:
        pass
    return "Bilinmiyor"

def is_host_alive(ip):
    """ICMP ping ile cihazın canlı olup olmadığını kontrol eder."""
    try:
        icmp = scapy.ICMP()
        ip_pkt = scapy.IP(dst=ip)
        resp = scapy.sr1(ip_pkt/icmp, timeout=1, verbose=0)
        return resp is not None
    except Exception:
        return False

def scan_network(ip_range, debug=False):
    try:
        nm = nmap.PortScanner(nmap_search_path=(NMAP_PATH,))
        nm.scan(ip_range, arguments='-T4 -F -O')
        devices = []
        for ip in nm.all_hosts():
            mac_address = nm[ip]['addresses'].get('mac', 'Bilinmiyor')
            os_info = nm[ip].get('osmatch', [])
            devices.append({'ip': ip, 'mac': mac_address, 'os': os_info})
        return devices
    except Exception as e:
        if debug:
            import traceback
            traceback.print_exc()
        print(f"Ağ taraması sırasında bir hata oluştu: {e}")
        return []

def scan_ports(ip_address, debug=False):
    try:
        nm = nmap.PortScanner(nmap_search_path=(NMAP_PATH,))
        nm.scan(ip_address, arguments='-T4 -p 21,22,80,139,443,3389 -sV')
        open_ports = []
        for port in nm[ip_address].get('tcp', {}):
            if nm[ip_address]['tcp'][port]['state'] == 'open':
                service = nm[ip_address]['tcp'][port]['name']
                version = nm[ip_address]['tcp'][port]['version']
                open_ports.append({'port': port, 'service': service, 'version': version})
        return open_ports
    except Exception as e:
        if debug:
            import traceback
            traceback.print_exc()
        print(f"{ip_address} için port taraması sırasında bir hata oluştu: {e}")
        return []

def save_to_csv(devices, filename="network_scan_results.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['IP', 'MAC', 'Hostname', 'Best OS Match', 'OS Accuracy', 'Open Ports']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for device in devices:
            best_os = None
            best_accuracy = 0
            for os_match in device['os']:
                try:
                    accuracy = int(os_match['accuracy'])
                    if accuracy > best_accuracy:
                        best_accuracy = accuracy
                        best_os = os_match
                except:
                    pass
            os_name = best_os['name'] if best_os else "Bilinmiyor"
            os_accuracy = best_os['accuracy'] if best_os else ""
            ports = "; ".join([f"{p['port']}({p['service']})" for p in device.get('open_ports', [])]) or "Yok"
            writer.writerow({
                'IP': device['ip'],
                'MAC': device['mac'],
                'Hostname': device.get('hostname', 'Bilinmiyor'),
                'Best OS Match': os_name,
                'OS Accuracy': os_accuracy,
                'Open Ports': ports
            })

def parse_args():
    parser = argparse.ArgumentParser(description='Ağ tarayıcı')
    parser.add_argument('--iprange', type=str, help='Tarama yapılacak IP aralığı (örn: 192.168.1.0/24)')
    parser.add_argument('--debug', action='store_true', help='Hata ayıklama modunu etkinleştir')
    return parser.parse_args()

def main():
    args = parse_args()
    debug = args.debug

    if args.iprange:
        ip_range = args.iprange
    else:
        gateway_ip = get_default_gateway_ip()
        if not gateway_ip:
            print("Ağ geçidi bulunamadığı için program sonlandırılıyor.")
            return
        ip_range = get_network_range(gateway_ip)
        if not ip_range:
            print("Ağ aralığı belirlenemediği için program sonlandırılıyor.")
            return

    print(f"Ağ {ip_range} taranıyor...")
    start_time = time.time()

    devices = scan_network(ip_range, debug=debug)

    print("\nCihazlar ping ile canlı mı kontrol ediliyor...")
    live_devices = []
    for device in tqdm(devices, desc="Ping Kontrolü"):
        if is_host_alive(device['ip']):
            live_devices.append(device)
        else:
            if debug:
                print(f"{device['ip']} yanıt vermedi.")

    print(f"\nCanlı cihaz sayısı: {len(live_devices)}")

    print("\nCihazların detaylı bilgileri toplanıyor (Hostname, Portlar, OS)...")
    for device in tqdm(live_devices, desc="Detaylı Tarama"):
        hostname = get_hostname(device['ip'])
        device['hostname'] = hostname

        open_ports = scan_ports(device['ip'], debug=debug)
        device['open_ports'] = open_ports

    # Özet istatistikler
    total_ports = sum(len(d.get('open_ports', [])) for d in live_devices)
    max_open_ports = 0
    ip_max_ports = "Yok"
    for d in live_devices:
        if len(d.get('open_ports', [])) > max_open_ports:
            max_open_ports = len(d['open_ports'])
            ip_max_ports = d['ip']

    elapsed = time.time() - start_time
    print(f"\nTarama tamamlandı. Toplam süre: {elapsed:.2f} saniye\n")
    print(f"Toplam canlı cihaz: {len(live_devices)}")
    print(f"Toplam açık port sayısı: {total_ports}")
    print(f"En çok açık port olan cihaz: {ip_max_ports} ({max_open_ports} port)")

    save_to_csv(live_devices)
    print("Sonuçlar 'network_scan_results.csv' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()
