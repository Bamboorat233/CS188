from util import Stack
from util import Queue

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def factorial_iterative(n):
    stack = Stack()
    result = 1
    
    # 模拟递归压栈
    while n > 0:
        stack.push(n)
        n -= 1

    # 模拟递归出栈
    while not stack.isEmpty():
        result *= stack.pop()

    return result

def dfs(graph, start):
    visited = set()
    stack = Stack()
    stack.push(start)

    while not stack.isEmpty():
        node = stack.pop()
        if node not in visited:
            print("访问节点:", node)
            visited.add(node)

            # 把相邻节点压入栈（注意：反向压入才能保持与递归一致的顺序）
            # reversed() 函数是对这个列表的反向遍历
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.push(neighbor)

def bfs_graph(graph: dict, start):
    """
    graph  : {节点: [相邻节点, …]}
    start  : 起始节点
    return : 按 BFS 访问顺序排列的节点列表
    """
    visited = set([start])
    order   = []            # 记录访问顺序
    q = Queue()
    q.push(start)

    while not q.isEmpty():
        node = q.pop()
        order.append(node)
        for nbr in graph.get(node, []): # 从字典 graph 里取出键 node 对应的邻接表（即所有相邻顶点组成的列表）
            if nbr not in visited:
                visited.add(nbr)
                q.push(nbr)
    return order


# ———— DEMO ————
if __name__ == "__main__":
    G = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [], 'E': ['F'], 'F': []
    }
    print(bfs_graph(G, 'A'))   # ➜ ['A', 'B', 'C', 'D', 'E', 'F']