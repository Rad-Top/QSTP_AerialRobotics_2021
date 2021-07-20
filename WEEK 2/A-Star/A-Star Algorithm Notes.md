# A-Star Algorithm
A* search is a combination of the Uniform Cost Search and the Greedy Search
- Uniform Cost Search  
    Each edge has a cost and the algorithm tries to find the way, by minimizing the accumulated cost of travel (g)
- Greedy Search  
    Takes the heuristic(h) into account

A* algorithm uses the sum of the accumulated path cost(g) and the heuristic(h) to calculate the path

- Assumes that the start and end poses are known
- Assumes that a map of the environment(often a grid map) is available
- The heuristic(often the straight line distance) speeds up the search

## A*: Minimize the Acculmulated Cost and the Estimated Cost

*g(n)* = Actual accumulated cost from the initial state to n
*h(n)* = estimated cost from the state n to the goal.

**f(n) = g(n) + h(n)** the estimated cost of the cheapest solution through *n*

## Heuristic for A*

- Let h*(n) be the actual cost of the optimal path from n to the next goal.

- We choose h(n) such that: **h(n) $\leq$ h\*(n)**

- We are always allowed to **Underestimate** the actual cost, not overestimate it.

- Ideally, h(n) must be as close as possible to h*

- An admissable heuristic is the euclidian straiht-line distance between the current point and the next goal.

- If we overestimate the heuristic, we loose the sense of optimality in the solution, but get a faster search 

## A* : Flow Chart
<img src="WEEK 2\A-Star\A Star Flow Chart.png" style="height: 100px; width:100px;"/>

## Assumptions in A*
1. The robot knows its own position
2. The robot computes its path based on the correct map
3. The correct motion commands are always executed

## Potential Problems

1. Robot is slightly Delocalised
2. Shortest path often guides the robot close to the objects: Can be solved by expanding the obstacles but this can cause problems in narrow passageways
3. Allignment of the planned trajectory and the grid structure of the map

## Convolution of the Grid Map

- Convulation is basically a gausian blur on the map.
- Averages the occupancy of the surrounding gridsn turning sharp turns into some sort of more blurred edges and smoothing out any edges that might be prestent
- A* is performed on the convolved map
- Increases **distance to obstacles** but the robot moves on a short path

- The Binomial Kernel Performs the blur as sgiven:
P(OCC<sub>x,y</sub>) = $\frac{1}{4}$.P(OCC<sub>x-1,y</sub>) + P(OCC<sub>x,y</sub>)






