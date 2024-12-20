# -*- coding: utf-8 -*-
"""Packet Sniffer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d0V6pFJ0rlvGN09T8TNdD1hAilNXQy0C
"""

pip install scapy

from scapy.all import sniff

# Define a packet handler function to analyze each packet
def packet_handler(packet):
    # Print summary of the packet
    print(packet.summary())

    # For detailed inspection, you can use packet.show()
    # packet.show()

# Capture network packets on interface 'eth0'
# You can change the interface as per your system (e.g., 'wlan0' for WiFi)
sniff(iface="eth0", prn=packet_handler, count=10)

def packet_handler(packet):
    if packet.haslayer('IP'):
        print(f"Source IP: {packet['IP'].src}")
        print(f"Destination IP: {packet['IP'].dst}")

    if packet.haslayer('TCP'):
        print(f"Source Port: {packet['TCP'].sport}")
        print(f"Destination Port: {packet['TCP'].dport}")