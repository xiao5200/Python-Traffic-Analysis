import pandas as pd
import matplotlib.pyplot as plt


def plot_protocol_distribution(file_path="data/analyzed_data.csv"):
    print("正在生成协议分布图表...")
    df = pd.read_csv(file_path)
    protocol_counts = df["协议类型"].value_counts()
    protocol_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("协议类型分布")
    plt.show()
    print("协议分布图表生成完成。")


if __name__ == "__main__":
    plot_protocol_distribution()
