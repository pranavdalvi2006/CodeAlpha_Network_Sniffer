from scapy.all import sniff, IP, IPv6, TCP, UDP
from datetime import datetime

print("Welcome to My Network Sniffer!")
print("Network packet capturing started...\n")

def show_packet(packet):

    print("\nNew Packet Captured!")
    print("------------------------")

    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

    elif packet.haslayer(IPv6):
        print("Source IP:", packet[IPv6].src)
        print("Destination IP:", packet[IPv6].dst)

    if packet.haslayer(TCP):
     print("Protocol: TCP")
     print("Source Port:", packet[TCP].sport)
     print("Destination Port:", packet[TCP].dport)

    elif packet.haslayer(UDP):
     print("Protocol: UDP")
     print("Source Port:", packet[UDP].sport)
     print("Destination Port:", packet[UDP].dport)

    print("Packet Summary:", packet.summary())
    print("Packet Size:", len(packet), "bytes")

print("Capture Started At:", datetime.now())
    
sniff(prn=show_packet, count=10)
print("Capture Ended At:", datetime.now())

print("\nPacket capturing completed!")