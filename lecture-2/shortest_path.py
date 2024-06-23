# Shortest Path Algorithm
# uninformed search algorithm to find shortest path for a graph with uniform costs

# start - start / beginner vertex
# successor - function, that returns adjacent vertices and weight of the edges if weighted graph
# is_goal -  function, that checks if adjacent vertex is the goal state
# Frontier: Contains all non-visited successors of previously visited states. Sorted by path length in ascending order.

# Visited states will NOT be visited again. Algorithm picks first element of the frontier and expands
# (going through its successors). A successor might be a goal state -> algorithm returns successfull path
# If not, new state is added to the end of the frontier. Each state in the frontier contains the entire path
# and corresponding actions that lead to it

# Highly generic example
def shortest_path_search(start, successors, is_goal):

    if is_goal(start):
        return [start]

    frontier = [[start]]  # Will contain nested lists for paths later
    explored = set([start])  # Set is unordered -> search more efficiently

    while frontier:  # As long as goal is not reached yet
        path = frontier.pop(0)  # Remove most left item in frontier
        s = path[-1]  # Newest state
        # Execute successors function -> Needs to be developed individually
        successors(s)
        for (state, action) in successors(s).items():  # state
            if state not in explored:
                explored.add(state)
                path_2 = path + [action, state]
            else:
                frontier.append(path_2)

    return [path_2]
