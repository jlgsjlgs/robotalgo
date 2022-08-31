from obstacle import Obstacle
from node import Node
import sys

# Task 1 - Exhaustive Search to find optimal Hamiltonian Path

def generatePermutations(numNodes): # Generates all possible permutation of visiting numNodes amount of obstacles
    tempstring1 = ""
    tempstring2 = ""
    permutationlist = []
    for i in range(1,numNodes+1):
        tempstring1 += str(i)
    permutate(tempstring1, tempstring2, permutationlist)
    return permutationlist

def permutate(s, answer, permutationlist): # Permutation function
    if len(s) == 0:
        permutationlist.append(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permutate(rest, answer + ch, permutationlist)

def generateGraph(obslist): # Generate adjacent matrix using manhattan distance between each obstacle
    source = (20,340)
    manhattandist = [[] for i in range(len(obslist)+1)]

    for i in range(len(obslist)+1):
        manhattandist[i] = [0] * (len(obslist)+1)

    for i in range(len(obslist)):
        for j in range(len(obslist)):
            if i == j:
                continue
            else:
                edgecost = abs(obslist[i].goalx - obslist[j].goalx) + abs(obslist[i].goaly - obslist[j].goaly)
                manhattandist[i][j] = edgecost
                manhattandist[j][i] = edgecost
    
    for i in range(len(obslist)):
        manhattandist[len(obslist)][i] = abs(obslist[i].goalx - source[0]) + abs(obslist[i].goaly - source[1])

    return manhattandist

def exhaustiveSearch(obslist): # Function that performs exhaustive search and returns the optimal path for visiting all obstacles
    g = generateGraph(obslist) # Note that last subarray = source node
    permutations = generatePermutations(len(obslist))
    lowestcost = sys.maxsize
    lowestcostpath = ""
    
    for i in permutations:
        firstNode = True
        currentCost=0
        prevNode = len(obslist) #Put source node as filler, we just want to instantiate prevNode here
        for nodes in i:
            if firstNode == True:
                firstNode = False
                currentCost += g[len(obslist)][int(nodes)-1]
            else:
                currentCost += g[prevNode-1][int(nodes)-1]
            prevNode = int(nodes)
        
        if currentCost < lowestcost:
            lowestcost = currentCost
            lowestcostpath = i
    
    print(g)
    print("Lowest cost found = {}, with path as {}".format(lowestcost,lowestcostpath))
    return lowestcostpath

# Task 2 - Astar search algorithm that our robot will use to traverse the maze 

def astarsearch(obslist):
    path = exhaustiveSearch(obslist)
    firstObs = True
    nextsource = None
    robotpathing = []

    for goals in path:
        if firstObs == True:
            firstObs = False
            source = Node(20,340,None,obslist[int(goals)-1])
        else:
            source = Node(nextsource.x, nextsource.y, None, obslist[int(goals)-1])

        openlist = []
        closedlist = []
        goalreached = False
        openlist.append(source)

        while len(openlist)!=0 and goalreached != True:
            #Find node with least F(n) on open list -> This node will be our next traversal
            nextnode = openlist[0]
            for temp in openlist:
                if temp.fn < nextnode.fn:
                    nextnode = temp
            
            #Pop nextnode off the open list
            openlist.remove(nextnode)
            openlist.clear()

            #Generate next set of successor nodes and set their parents to nextnode
            nextmoveset = findSuccessors(nextnode, obslist)
            
            for movement in nextmoveset:
                if movement == "L":
                    tempnode = Node(nextnode.x-20, nextnode.y, nextnode, obslist[int(goals)-1])
                elif movement == "R":
                    tempnode = Node(nextnode.x+20, nextnode.y, nextnode, obslist[int(goals)-1])
                elif movement == "U":
                    tempnode = Node(nextnode.x, nextnode.y-20, nextnode, obslist[int(goals)-1])
                elif movement == "D":
                    tempnode = Node(nextnode.x, nextnode.y+20, nextnode, obslist[int(goals)-1])
                
                # If successor is goal, end current iteration and move on to next goal
                if tempnode.x == obslist[int(goals)-1].goalx and tempnode.y == obslist[int(goals)-1].goaly:
                    goalreached = True
                    nextsource = tempnode
                    break

                # If a node with same position already exists in OPEN list, and it has lower f(n), skip this successor
                skipNode = False
                for opennodes in openlist:
                    if opennodes.x == tempnode.x and opennodes.y == tempnode.y and opennodes.fn < tempnode.fn:
                        skipNode = True
                        break
                
                if skipNode == True:
                    continue

                # If node with same position already exists in CLOSED list, and it has lower f(n), skip this successor, otherwise add it to open list
                for closednodes in closedlist:
                    if closednodes.x == tempnode.x and closednodes.y == tempnode.y and closednodes.fn < tempnode.fn:
                        skipNode = True
                        break
                
                if skipNode != True:
                    openlist.append(tempnode)

            closedlist.append(nextnode)
        
        closedlist.append(nextsource)
        robotpathing.append(closedlist)
    
    return robotpathing

  
def findSuccessors(curnode, obslist): # Function to find all possible nodes that robot can go next
    successors = []

    if curnode.x-20 >= 20 and obstacleAvoidance(curnode.x-20, curnode.y, obslist):
        successors.append("L")
    
    if curnode.x+20 <= 360 and obstacleAvoidance(curnode.x+20, curnode.y, obslist):
        successors.append("R")

    if curnode.y-20 >= 20 and obstacleAvoidance(curnode.x, curnode.y-20, obslist):
        successors.append("U")
    
    if curnode.y+20 <= 360 and obstacleAvoidance(curnode.x, curnode.y+20, obslist):
        successors.append("D")
            
    return successors


def obstacleAvoidance(x, y, obslist): # Checks for a given node, if the center of the robot were to be there, will it bump into any obstacles
    boundaries = [[x-20, y-20], [x, y-20], [x+20, y-20],
                [x-20, y], [x, y], [x+20, y],
                [x-20, y+20], [x, y+20], [x+20, y+20]]
    
    for obs in obslist:
        for positions in boundaries:
            if obs.x == positions[0] and obs.y == positions[1]:
                return False
    return True
    