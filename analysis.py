import os
import pyshark
import pandas as pd

# 设置 tshark 的路径
tshark_path = r'D:\software\Wireshark\tshark.exe'

def analyze_pcap(file_path="data/captured_traffic.pcap"):
    print("正在分析PCAP文件中的流量数据...")
    try:
        # 使用指定的 tshark 路径创建 FileCapture 对象
        packets = pyshark.FileCapture(file_path, tshark_path=tshark_path)
        data = []
        for packet in packets:
            if 'IP' in packet:
                src = packet.ip.src
                dst = packet.ip.dst
                protocol = packet.transport_layer
                length = int(packet.length)
                data.append([src, dst, protocol, length])

        df = pd.DataFrame(data, columns=["源IP", "目标IP", "协议类型", "数据包长度"])
        df.to_csv("data/analyzed_data.csv", index=False)
        print("分析完成，结果已保存到 'data/analyzed_data.csv'。")
        return df
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    analyze_pcap()