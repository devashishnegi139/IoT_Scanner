# scan_network.py
# this script scans the local network to find connected devices and returns their IP addresses and MAC addresses
from scapy.all import ARP, Ether, srp
def scan(subnet):
    # Create an ARP request packet
    arp = ARP(pdst=subnet)
    
    # Create an Ethernet frame to broadcast the ARP request
    # The destination MAC address is set to the broadcast address
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    
    # Combine the Ethernet frame and ARP request into a single packet
    # The ARP request will be sent to all devices in the specified subnet
    packet = ether / arp

    # Send the packet on the network and wait for responses
    # The srp function sends and receives packets at the link layer
    # Send the packet and receive the response
    ans = srp(packet, timeout=2, verbose=False)[0]

    # Extract IP and MAC addresses from the response
    devices = []
    for sent, received in ans:
        # Append the IP and MAC address to the devices list
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices