import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def bfs_levels(graph, start):
    visited = []
    levels = {}
    queue = [(start, 0)]
    while queue:
        node, level = queue.pop(0)
        if node not in visited:
            visited.append(node)
            levels[node] = level
            neighbours = set(graph[node]) - set(visited)
            queue.extend([(neighbour, level + 1) for neighbour in neighbours])
    return visited, levels

def update(frame):
    ax.clear()
    
    # Draw all nodes
    for node, position in pos.items():
        ax.scatter(*position, color='skyblue', s=500)
        ax.text(*position, node, color='black', fontsize=12, ha='center', va='center')
    
    # Draw all edges
    for node, neighbours in graphe.items():
        for neighbour in neighbours:
            node_pos = np.array(pos[node])
            neighbour_pos = np.array(pos[neighbour])
            ax.plot([node_pos[0], neighbour_pos[0]], [node_pos[1], neighbour_pos[1]], 'gray')
    
    # Highlight visited nodes with different colors based on levels
    for i in range(frame + 1):
        node = bfs_path[i]
        node_position = pos[node]
        level = levels[node]
        color = colors[level % len(colors)]
        ax.scatter(*node_position, color=color, s=500)
    
    # Title
    ax.set_title('Animation: Frame {}'.format(frame))
    ax.axis('off')

graphe = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'F'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F', 'G'],
    'E': ['C', 'D'],
    'F': ['B', 'D', 'G'],
    'G': ['D', 'F','E']
}

pos = {
    'A': (0, 1), 'B': (1, 2), 'C': (1, 0), 'D': (2, 1),
    'E': (3, 0), 'F': (3, 2), 'G': (4, 1)
}

# BFS path and levels
start_node = 'A'
bfs_path, levels = bfs_levels(graphe, start_node)

# Define colors for levels
colors = ['orange', 'red', 'green', 'blue', 'purple', 'yellow', 'cyan']

# Create plot
fig, ax = plt.subplots()

# Create animation
ani = FuncAnimation(fig, update, frames=len(bfs_path), interval=1000, repeat=False)

# Show animation
plt.show()
