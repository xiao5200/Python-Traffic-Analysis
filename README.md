# 基于Python的网络流量监控与分析系统

## 项目简介

本项目是一个基于Python的网络流量监控与分析系统，旨在通过实时捕获、分析和可视化网络流量，帮助用户更好地监控网络状态，识别异常流量活动。项目包含流量捕获、数据分析、可视化展示和报警模块，适用于网络安全分析、流量监控等场景。

## 主要功能

- **或流量捕获**：使用ScapyPyShark从网络接口中捕获流量，并将其保存为PCAP文件。
- **数据分析**：解析PCAP文件，提取流量中的关键信息（如源IP、目标IP、协议类型等），并进行统计分析。
- **可视化展示**：生成协议分布饼图、流量随时间变化的折线图等图表，直观展示分析结果。
- **报警通知**：检测异常流量，并在超过设定值时触发报警通知。

## 项目结构

```
├── capture.py         # 流量捕获模块
├── analysis.py        # 流量分析模块
├── visualize.py       # 数据可视化模块
├── alert.py           # 报警模块
├── app.py             # Web应用入口
├── static/            # 存放Web应用的静态文件（如CSS、JavaScript）
├── templates/         # 存放Web应用的HTML模板
├── data/              # 存放捕获的PCAP文件和日志
└── README.md          # 项目说明文档
```

## 安装步骤

### 1 安装依赖

确定安装Python 3.x，已推荐使用虚拟环境。安装依赖库：

```
pip install -r requirements.txt
```

`requirements.txt`内容如下：

```
pyshark
pandas
matplotlib
flask
```

### 2.准备网络环境

建议使用**GNS3**或**Wireshark**创建一个虚拟网络环境，方便测试系统的流量捕获和分析功能。

## 使用方法

### 1. 流量捕获

运行流量`capture.py`开始捕获流量，捕获捕获的保存到PCAP文件：

```
python capture.py
```

捕获完成后，PCAP文件将保存到`data/`目录下。

### 2. 分析师

运行`analysis.py`对采集的PCAP文件进行数据分析，提取关键信息并保存到CSV文件：

```
python analysis.py
```

结果将保存到`data/analyzed_data.csv`。

### 3. 数据可视化

运行`visualize.py`生成分析结果的图表（如协议分配饼图）并展示：

```
python visualize.py
```

### 4. 报警检测

运行`alert.py`检查分析结果是否存在异常流量，若超过阈值则发送报警通知：

```
python alert.py
```

### 5. 网站展示

运行`app.py`启动Flask Web应用，将图表嵌入Web界面显示：

```
python app.py
```

打开浏览器访问`http://127.0.0.1:5000`查看图表和数据分析结果。

##web页面代码自行添加
index.html
```
{% extends "layout.html" %}

{% block content %}
<h2>网络流量协议类型分布</h2>
<div class="chart">
    <img src="{{ url_for('static', filename='images/protocol_distribution.png') }}" alt="协议类型分布图">
</div>
<div class="data">
    <h3>流量统计信息</h3>
    <p>此处可以显示更多统计数据，如访问量前五的IP地址等。</p>
</div>
{% endblock %}
```
layout.html
```
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>网络流量监控与分析系统</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header>
        <h1>网络流量监控与分析系统</h1>
    </header>
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 网络流量监控系统</p>
    </footer>
    
    <script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
</body>
</html>

```

## 主要模块说明

### 1.`capture.py`

流量捕获模块，使用Scapy监听指定的网络接口，按设置的过滤条件捕获流量，将捕获的数据保存为PCAP格式文件，随后进行后续分析。

### 2.`analysis.py`

数据分析模块，使用PyShark读取PCAP文件，提取IP地址、端口、协议类型等信息，并使用Pandas将数据转化为数据框格式，进行统计分析后保存为CSV文件。

### 3.`visualize.py`

可视化模块，使用Matplotlib生成分析结果的图表，包括协议类型分布、IP访问量柱状图等。可视化结果供用户放大查看流量分布和趋势。

### 4.`alert.py`

报警模块，分析数据中是否存在异常流量，如果发现流量超过设定阈值，将触发报警。支持通过电子邮件或Webhook发送报警通知。

### 5.`app.py`

Web应用模块，使用Flask构建一个简单的Web界面，将可视化图表嵌入页面，方便用户查看数据分析结果。

## 测试与优化

本系统已在虚拟网络环境中进行测试，主要测试流量捕获、分析准确性和报警功能。为优化系统性能，部分数据处理和绘图代码针对已大规模数据进行改进。

## 注意事项

- 运行项目需要管理员权限以访问网络接口。
- 建议在虚拟网络环境中进行测试，确保不影响实际网络环境。
