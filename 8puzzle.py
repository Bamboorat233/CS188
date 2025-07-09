# 8数码游戏界面与A*求解器的实现

# Part 1: 游戏状态定义和工具函数
from typing import List, Tuple, Optional
import heapq

# 游戏目标状态
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# 检查两个状态是否相同
def is_goal(state: List[List[int]]) -> bool:
    return state == GOAL_STATE

# 获取空格（0）的位置
def find_zero(state: List[List[int]]) -> Tuple[int, int]:
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# 计算曼哈顿距离启发函数
def manhattan(state: List[List[int]]) -> int:
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value == 0:
                continue
            target_x = (value - 1) // 3
            target_y = (value - 1) % 3
            dist += abs(i - target_x) + abs(j - target_y)
    return dist

# 状态的唯一键（字符串形式）
def state_to_key(state: List[List[int]]) -> str:
    return ''.join(str(cell) for row in state for cell in row)

# 移动空格（上下左右）
def get_neighbors(state: List[List[int]]) -> List[List[List[int]]]:
    x, y = find_zero(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Part 2: A* 算法实现
def astar(start: List[List[int]]) -> Optional[List[List[List[int]]]]:
    open_set = []
    heapq.heappush(open_set, (manhattan(start), 0, start, [start]))  # (f, g, current, path)
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        key = state_to_key(current)
        if key in visited:
            continue
        visited.add(key)

        if is_goal(current):
            return path  # 返回路径

        for neighbor in get_neighbors(current):
            if state_to_key(neighbor) not in visited:
                heapq.heappush(open_set, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [neighbor]))

    return None

# 示例初始状态（有解）
example_start = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

solution_path = astar(example_start)

import pandas as pd
if solution_path:
    steps = ['\n'.join([' '.join(str(cell) for cell in row) for row in state]) for state in solution_path]
    df = pd.DataFrame({'Step': range(len(steps)), 'State': steps})
else:
    df = pd.DataFrame({'Step': [], 'State': []})

for step, state in enumerate(solution_path):
    print(f"Step {step}:")
    for row in state:
        print(row)
    print()

