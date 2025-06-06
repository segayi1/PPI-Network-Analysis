~~~markdown
# Protein-Protein Interaction Network Analysis Toolkit
## 📌 项目概述

本工具包提供蛋白质相互作用网络(PPI)的自动化分析解决方案，主要功能包括：
- 多源PPI数据加载与预处理
- 交互网络图构建与归一化处理
- 蛋白质间最短路径分析
- 关键节点识别与局部网络可视化

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
# 或手动安装核心依赖
pip install pandas networkx matplotlib numpy
~~~

### 运行演示

```bash
# 生成测试数据（可选）
python generate_test_data.py

# 启动交互式分析界面
python main.py
```

## 🛠️ 核心功能

| 命令                            | 功能描述               | 示例用法                                             |
| ------------------------------- | ---------------------- | ---------------------------------------------------- |
| `load <path>`                   | 加载数据文件(.txt/.gz) | `load data/9606.protein.links.detailed.v12.0.txt.gz` |
| `build_graph`                   | 构建交互网络图         | 自动执行                                             |
| `print_graph`                   | 显示网络基本信息       | 查看节点/边数量                                      |
| `query_distance P1 P2`          | 查询蛋白质间最短路径   | `query_distance P05362 P00441`                       |
| `find_nearest P1 [N] [K]`       | 查找K层内最近的N个邻居 | `find_nearest P09958 5 2`                            |
| `get_local_centralities P1 [K]` | 计算K层局部中心性指标  | `get_local_centralities P01375 3`                    |
| `draw_subgraph`                 | 交互式绘制子网络       | 按提示输入蛋白质列表                                 |
| `exit`                          | 退出程序               |                                                      |

## 📂 文件结构

```markdown
PPI_Toolkit/
├── main.py                    # 主程序入口
├── ppi_processor.py           # 核心处理类
├── generate_test_data.py      # 测试数据生成器
├── data/
│   └── test_ppi_data.txt      # 示例数据
└── requirements.txt           # 依赖列表
```

## 🧪 测试数据说明

使用`generate_test_data.py`可生成标准格式的模拟数据：

```python
# 生成10000个蛋白质对的测试集
python generate_test_data.py -n 10000
```

生成数据包含以下特征：

- 蛋白质ID（6位编码）
- 7种相互作用证据分数
- 综合评分(combined_score)

## 💡 高级用法

### 批量模式运行

```python
# 在Python中直接调用处理器
from ppi_processor import PPI_processor

processor = PPI_processor("data.txt.gz")
processor.build_graph()
results = processor.find_nearest_proteins("P12345", n=10, k=3)
```

### 自定义归一化范围

```python
# 修改ppi_processor.py中的归一化参数
def normalize_values(self, index='combined_score', new_min=0, new_max=1000):
    """自定义归一化范围"""
    ...
```

## 📊 典型输出示例

1. 最短路径分析结果：

```markdown
蛋白质 P12345 和 P67890 之间的最短路径长度为：2.34
路径为：['P12345', 'P55678', 'P67890']
路径置信度：[825, 790]
```

1. 局部中心性分析：
    | Protein   | Degree | Betweenness |
    |-----------|--------|-------------|
    | P09958    | 142    | 0.156       |
    | P01375    | 98     | 0.121       |

## 📜 许可证

本项目采用 MIT License

## 🤝 如何贡献

1. Fork本项目
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

## 📬 联系作者

如有技术问题或合作意向，请联系：

- Email: choir_cloud@sjtu.edu.cn ,  segayi1@sjtu.edu.cn

```markdown

### 关键特点说明：
1. **模块化设计**：核心功能封装在`ppi_processor.py`，支持单独调用
2. **灵活输入**：支持压缩文件(.gz)和原始文本
3. **动态交互**：通过`main.py`提供用户友好的命令行界面
4. **可扩展性**：可轻松添加新的分析算法（如社区发现）
```

