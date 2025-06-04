# scan_network.py
from scapy.all import ARP, Ether, srp
def scan(subnet):
    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    ans = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for sent, received in ans:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices