class State:
    def __init__(self, value, heuristic):
        self.value = value
        self.heuristic = heuristic

def hill_climbing(current_state, goal_state):
    while True:
        print("Current State:", current_state.value)
        if current_state.heuristic == goal_state.heuristic:
            return current_state.value
        
        neighbors = get_neighbors(current_state)
        next_state = get_best_neighbor(neighbors, goal_state)
        
        if next_state.heuristic >= current_state.heuristic:
            return current_state.value
        
        current_state = next_state

def get_neighbors(state):
    # In a real implementation, you'd generate neighboring states based on current state
    # For simplicity, let's assume a list of predefined neighboring states
    # You can modify this part according to your problem
    neighbors = [
        State("Neighbor 1", 5),
        State("Neighbor 2", 7),
        State("Neighbor 3", 3)
    ]
    return neighbors

def get_best_neighbor(neighbors, goal_state):
    best_neighbor = min(neighbors, key=lambda x: x.heuristic)
    return best_neighbor

# Define the initial and goal states
initial_state = State("Initial State", 10)
goal_state = State("Goal State", 0)

# Perform hill climbing algorithm
result = hill_climbing(initial_state, goal_state)

print("Reached:", result)
