# Shortest Path Algorithm
# uninformed search algorithm to find shortest path for a graph with uniform costs
# start - start state
# successor - function that returns the successor of a state and the corresponding actions
# is_goal - function that returns true if a state is a goal

# Frontier: Contains all non-visited successors of previously visited states. Sorted by path length in ascending order.
# Visited states will NOT be visited again. Algorithm picks first element of the frontier and expands
# (going through its successors). A successor might be a goal state -> algorithm returns successfull path
# If not, new state is added to the end of the frontier. Each state in the frontier contains the entire path
# and corresponding actions that lead to it
