from util import Stack
from util import Queue
from util import PriorityQueue

# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

class SimpleGraphSearchProblem:
    def __init__(self, graph, start, goal):
        self.graph = graph  # 字典：{ state: [(neighbor, cost), ...] }
        self.start = start
        self.goal = goal

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state == self.goal

    def getSuccessors(self, state):
        successors = []
        for neighbor, cost in self.graph.get(state, []):
            successors.append((neighbor, neighbor, cost))  # (state, action, cost)
        return successors


def uniformCostSearch(problem):
    frontier = PriorityQueue()
    frontier.push((problem.getStartState(), [], 0), 0)  # (state, path, cost)
    explored = set()

    while not frontier.isEmpty():
        state, path, cost = frontier.pop()

        if problem.isGoalState(state):
            return path

        if state not in explored:
            explored.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                newPath = path + [action]
                newCost = cost + stepCost
                frontier.update((successor, newPath, newCost), newCost)

    return []  # No path found


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# def factorial_iterative(n):
#     stack = Stack()
#     result = 1
    
#     # 模拟递归压栈
#     while n > 0:
#         stack.push(n)
#         n -= 1

#     # 模拟递归出栈
#     while not stack.isEmpty():
#         result *= stack.pop()

#     return result

# def dfs(graph, start):
#     visited = set()
#     stack = Stack()
#     stack.push(start)

#     while not stack.isEmpty():
#         node = stack.pop()
#         if node not in visited:
#             print("访问节点:", node)
#             visited.add(node)

#             # 把相邻节点压入栈（注意：反向压入才能保持与递归一致的顺序）
#             # reversed() 函数是对这个列表的反向遍历
#             for neighbor in reversed(graph[node]):
#                 if neighbor not in visited:
#                     stack.push(neighbor)

# def bfs_graph(graph: dict, start):
#     """
#     graph  : {节点: [相邻节点, …]}
#     start  : 起始节点
#     return : 按 BFS 访问顺序排列的节点列表
#     """
#     visited = set([start])
#     order   = []            # 记录访问顺序
#     q = Queue()
#     q.push(start)

#     while not q.isEmpty():
#         node = q.pop()
#         order.append(node)
#         for nbr in graph.get(node, []): # 从字典 graph 里取出键 node 对应的邻接表（即所有相邻顶点组成的列表）
#             if nbr not in visited:
#                 visited.add(nbr)
#                 q.push(nbr)
#     return order


# ———— DEMO ————
if __name__ == "__main__":
    # G = {
    #     'A': ['B', 'C'],
    #     'B': ['D', 'E'],
    #     'C': ['F'],
    #     'D': [], 'E': ['F'], 'F': []
    # }
    # print(bfs_graph(G, 'A'))   # ➜ ['A', 'B', 'C', 'D', 'E', 'F']
    problem = SimpleGraphSearchProblem(graph, 'A', 'D')
    path = uniformCostSearch(problem)
    print("Path found:", path)
