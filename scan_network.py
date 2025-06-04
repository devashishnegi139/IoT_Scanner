from scapy.all import ARP, Ether, srp

def scan(subnet):
    """
    Scans a given subnet using ARP and returns a list of active devices.

    Args:
        subnet (str): Target subnet or IP range, e.g., '192.168.1.0/24'.

    Returns:
        List[dict]: List of devices with 'ip' and 'mac' keys.
    """
    # Create broadcast Ethernet frame
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    # Create ARP request for the given subnet
    arp = ARP(pdst=subnet)

    # Combine Ethernet and ARP to form a complete packet
    packet = ether / arp

    # Send the packet and collect responses
    ans = srp(packet, timeout=2, verbose=False)[0]

    devices = []
    for _, received in ans:
        devices.append({
            'ip': received.psrc,      # Sender IP address
            'mac': received.hwsrc     # Sender MAC address
        })

    return devices
