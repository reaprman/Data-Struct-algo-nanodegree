""" g is the distance between the current point and the edge point.
    h is the straight line distance between the edge point and goal
 """
import math

def path_finder(paths, start, goal):
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = paths[curr]
    path.append(curr)

    return path.reverse()

def shortest_path(M_map,start,goal):
    frontier = dict()
    #changed var from set called explored to dict called scores
    scores = {start: 0}
    path[start] = None
    frontier[start] = 0
    goal_point = M_map.intersections[goal]
    
    while frontier:
        #no longer storing estimated length from frontier
        current_lowest = sorted(frontier.items(), key=lambda x: x[1])[0][0]
        if current_lowest == goal:
            return path_finder(path, start, goal) # break

        frontier.pop(current_lowest)
        for edge in M_map.roads[current_lowest]:
            #g cost + h cost 
            g = path_cost(M_map.intersections[current_lowest], M_map.intersections[edge])
            h = path_cost(M_map.intersections[edge], goal_point)
            # scores[current_lowest] is the path cost up to the current intersection
            # used actual distance score instead of estimated distance score for comparisons
            new_distance = scores[current_lowest] + g
            if (edge not in scores or new_distance < scores[edge]):
                scores[edge] = new_distance
                frontier[edge] = new_distance + h
                path[edge] = current_lowest
    return -1 # path_finder(path, start, goal)
    
    print("shortest path called")
    return

def path_cost(point1, point2): # 1/2 are list with x,y coordinate values

    return math.sqrt(((point2[0] - point1[0]) ** 2) + ((point2[1] - point1[1]) ** 2))
