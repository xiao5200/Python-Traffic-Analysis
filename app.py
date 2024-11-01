from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    plot_protocol_distribution()
    return render_template("index.html")


def plot_protocol_distribution():
    print("生成协议分布图表并保存为静态文件...")
    df = pd.read_csv("data/analyzed_data.csv")
    protocol_counts = df["协议类型"].value_counts()
    protocol_counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title("协议类型分布")
    plt.savefig("static/protocol_distribution.png")
    print("图表保存完成，已更新到静态文件。")


if __name__ == "__main__":
    app.run(debug=True)
