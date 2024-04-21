class Node:
    def __init__(self, value, parent=None, g=float('inf'), h=float('inf')):
        self.value = value
        self.parent = parent
        self.g = g  # Actual cost from start node to this node
        self.h = h  # Heuristic cost from this node to goal node

    def f(self):
        return self.g + self.h  # Total estimated cost


def a_star_search(graph, start_node, goal_node):
    open_set = [start_node]
    closed_set = []

    while open_set:
        open_set.sort(key=lambda x: x.f())  # Sort the open set based on total estimated cost
        current_node = open_set.pop(0)
        if current_node.value == goal_node.value:
            return current_node

        for neighbor in graph[current_node.value]:
            g = current_node.g + 1  # Assuming a cost of 1 for each edge
            h = calculate_heuristic(neighbor, goal_node.value)
            neighbor_node = Node(neighbor, current_node, g, h)
            if neighbor_node not in closed_set:
                open_set.append(neighbor_node)
                closed_set.append(neighbor_node)

    return None


def calculate_heuristic(node_value, goal_value):
    # For simplicity, let's assume a heuristic where the cost is the absolute difference between node and goal values
    return abs(ord(node_value) - ord(goal_value))


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

    start_node_obj = Node(start_node, None, 0, calculate_heuristic(start_node, goal_node))  # Start node with g=0
    goal_node_obj = Node(goal_node, None, float('inf'), 0)  # Goal node with h=0

    result = a_star_search(graph, start_node_obj, goal_node_obj)

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


