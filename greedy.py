class Node:
    def __init__(self, value, parent=None, heuristic=float('inf')):
        self.value = value
        self.parent = parent
        self.heuristic = heuristic

def greedy_best_first_search(graph, start_node, goal_node):
    open_set = [start_node]
    closed_set = []

    while open_set:
        open_set.sort(key=lambda x: x.heuristic)  # Sort the open set based on heuristic
        current_node = open_set.pop(0)
        if current_node.value == goal_node.value:
            return current_node

        for neighbor in graph[current_node.value]:
            neighbor_node = Node(neighbor, current_node)
            if neighbor_node not in closed_set:
                open_set.append(neighbor_node)
                closed_set.append(neighbor_node)

    return None

# Ask the user to input the graph matrix
def create_graph_from_input():
    graph = {}
    nodes = input("Enter nodes separated by space: ").split()
    for node in nodes:
        neighbors = input(f"Enter neighbors for node {node}: ").split()
        graph[node] = neighbors
    return graph

# Ask the user to input the start node and the goal node
def get_start_and_goal_nodes():
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    return start_node, goal_node

# Main function
def main():
    graph = create_graph_from_input()
    start_node, goal_node = get_start_and_goal_nodes()

    start_node_obj = Node(start_node, None, 0)  # Start node with heuristic 0
    goal_node_obj = Node(goal_node, None, float('inf'))  # Goal node with heuristic infinity

    result = greedy_best_first_search(graph, start_node_obj, goal_node_obj)

    if result:
        path = []
        while result:
            path.append(result.value)
            result = result.parent

        path.reverse()
        print('The path from start to goal is:', path)
    else:
        print('No path found from start to goal.')

if __name__ == "__main__":
    main()




