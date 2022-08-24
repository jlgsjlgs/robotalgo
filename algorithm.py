from obstacle import Obstacle
import sys

def generatePermutations(numNodes):
    tempstring1 = ""
    tempstring2 = ""
    permutationlist = []
    for i in range(1,numNodes+1):
        tempstring1 += str(i)
    permutate(tempstring1, tempstring2, permutationlist)
    return permutationlist

def permutate(s, answer, permutationlist):
    if len(s) == 0:
        permutationlist.append(answer)
        return
    
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i+1:]
        rest = left_substr + right_substr
        permutate(rest, answer + ch, permutationlist)

def generateGraph(obslist):
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

def exhaustiveSearch(obslist):
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

# def astarsearch(obslist):
    # exhaustiveSearch(obslist)


        


                


    
    
    