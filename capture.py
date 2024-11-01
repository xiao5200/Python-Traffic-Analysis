from scapy.all import sniff, wrpcap


def capture_packets(interface="eth0", filter="tcp", count=100):
    print(f"开始在接口 {interface} 上捕获流量，过滤条件为：{filter}...")
    packets = sniff(iface=interface, filter=filter, count=count)
    wrpcap("data/captured_traffic.pcap", packets)
    print("捕获完成，流量数据已保存到 'data/captured_traffic.pcap'。")


if __name__ == "__main__":
    capture_packets()
