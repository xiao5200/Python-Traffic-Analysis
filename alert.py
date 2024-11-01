import smtplib
from email.mime.text import MIMEText
import pandas as pd


def check_alerts(file_path="data/analyzed_data.csv", threshold=100):
    print("正在检查是否存在异常流量...")
    df = pd.read_csv(file_path)
    ip_counts = df["源IP"].value_counts()
    for ip, count in ip_counts.items():
        if count > threshold:
            send_alert(f"警报：IP地址 {ip} 的数据包数量超过阈值，共 {count} 个数据包。")
    print("检查完成。")


def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = "网络流量警报"
    msg['From'] = "sender@example.com"
    msg['To'] = "receiver@example.com"

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("username", "password")
        server.send_message(msg)
    print("警报已发送！")


if __name__ == "__main__":
    check_alerts()