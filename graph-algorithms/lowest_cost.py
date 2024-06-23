import heapq

# Lowest Cost Search
# Attributes:
# 1. start = starting vertex
# 2. successors = individually coded successors function
# 3. is_goal = individually coded function to check if current node is the goal node
# 4. action_cost = function to calculate the costs for the current action on weighted graph

# Helper Methods


def path_cost(path):
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


def add_to_frontier(frontier, path):
    heapq.heappush(frontier, (path_cost(path), path))


def lowest_cost_search(start, successors, is_goal, action_cost):

    explored = set()  # Set with already visited nodes
    # List of paths, waited to be expanded -> every path is an individual list of states
    frontier = [[start]]

    while frontier:  # as long as frontier is not empty

        # current path (list) will be removed from frontier
        path = frontier.pop(0)

        state_1 = path[-1]  # last state in current path (list)

        if is_goal(state_1):  # if the last state of current path is the goal
            return path  # return the first path (list) of frontier (list)

        explored.add(state_1)  # else add the last item to the explored list

        # calculate the current cost of the whole path -> Needs to be coded
        pcost = path_cost(path)

        # calculate the following states (successors)
        for (state, action) in successors(state_1).items():

            if state not in explored:  # if the successor state is not in explored yet

                # calculate the successors cost
                total_cost = pcost + action_cost(action)

                # calculate the other path
                path_2 = path + [(action, total_cost,), state]
                # add the new path to frontier again
                add_to_frontier(frontier, path_2)

    return []
