# main.py
import importlib
from ppi_processor import PPI_processor
import matplotlib.pyplot as plt
import networkx as nx

def main():
    print("欢迎使用蛋白质相互作用处理程序！")
    print("正在检查必要的包是否已安装...")


    print("支持的命令：")
    print("1. load <文件路径> - 加载数据文件")
    print("2. build_graph - 构建蛋白质相互作用图（自动完成归一化）")
    print("3. print_graph - 打印图的节点和边信息")
    print("4. query_distance <蛋白质1> <蛋白质2> - 查询两个蛋白质之间的最短路径和置信度")
    print("5. find_nearest <蛋白质> <最近邻居数量> <层数> - 查找指定蛋白质的最近邻居")
    print("6. get_local_centralities <蛋白质> <层数> - 计算指定蛋白质周围的中心性")
    print("7. draw_subgraph - 绘制包含指定蛋白质的子图")
    print("8. exit - 退出程序")

    processor = None
    must_load_and_build = True  # 标记是否必须优先执行load和build

    while True:
        if must_load_and_build:
            # 强制先执行load和build_graph
            print("\n【系统提示】请先完成数据加载和图构建：")
            if processor is None:
                # 自动执行load（使用默认路径或用户输入）
                file_path = input("请输入数据文件路径（直接回车使用默认路径）：").strip()
                if not file_path:
                    file_path = "D:\\codehomework\\project\\9606.protein.links.detailed.v12.0.txt.gz"
                    print(f"使用默认路径：{file_path}")
                
                processor = PPI_processor(file_path)
                if processor._data is None:
                    print("文件加载失败！")
                    continue
            
            # 自动执行build_graph
            processor.normalize_values()
            processor.graph_builder()
            print(">>> 图构建完成！现在可以自由选择后续操作 <<<")
            must_load_and_build = False
        else:
            # 显示可选的命令菜单
            print("\n" + "="*50)
            print("请选择要执行的操作（输入命令编号或名称）：")
            print("  [1] print_graph       - 打印图信息")
            print("  [2] query_distance    - 查询蛋白质间距离")
            print("  [3] find_nearest      - 查找最近邻居")
            print("  [4] get_local_centralities - 计算局部中心性")
            print("  [5] draw_subgraph     - 绘制子图")
            print("  [6] reload            - 重新加载数据")
            print("  [7] exit              - 退出程序")
            print("="*50)

        # 命令处理逻辑
        try:
            cmd = input("\n请输入命令：").strip().lower()
            if not cmd:
                continue

            if cmd in ['1', 'print_graph']:
                processor.print_graph_info()
                
            elif cmd in ['2', 'query_distance']:
                protein1 = input("请输入蛋白质1编号：").strip()
                protein2 = input("请输入蛋白质2编号：").strip()
                processor.query_protein_distance(protein1, protein2)
                
            elif cmd in ['3', 'find_nearest']:
                protein = input("请输入目标蛋白质编号：").strip()
                n = input("请输入要查找的邻居数量（默认5）：").strip()
                k = input("请输入搜索层数（默认3）：").strip()
                processor.find_nearest_proteins(
                    protein,
                    n=int(n) if n else 5,
                    k=int(k) if k else 3
                )
                
            elif cmd in ['4', 'get_local_centralities']:
                protein = input("请输入目标蛋白质编号：").strip()
                k = input("请输入搜索层数（默认3）：").strip()
                centrality_df = processor.calculate_local_centralities(
                    protein, 
                    k=int(k) if k else 3
                )
                if centrality_df is not None:
                    print(centrality_df.to_string())
                    
            elif cmd in ['5', 'draw_subgraph']:
                print("请输入要绘制的蛋白质编号（多个用空格分隔，回车结束）：")
                proteins = []
                while True:
                    line = input("> ").strip()
                    if not line:
                        break
                    proteins.extend(line.split())
                
                if proteins:
                    subgraph = processor._graph.subgraph(proteins)
                    pos = nx.spring_layout(subgraph)
                    nx.draw(subgraph, pos, with_labels=True)
                    plt.show()
                else:
                    print("未输入蛋白质编号！")
                    
            elif cmd in ['6', 'reload']:
                confirm = input("确定要重新加载数据吗？（y/n）").strip().lower()
                if confirm == 'y':
                    processor = None
                    must_load_and_build = True
                    
            elif cmd in ['7', 'exit']:
                print("程序已退出")
                break
                
            else:
                print("无效命令！请参考菜单输入")
                
        except Exception as e:
            print(f"执行出错：{str(e)}")

if __name__ == "__main__":
    main()