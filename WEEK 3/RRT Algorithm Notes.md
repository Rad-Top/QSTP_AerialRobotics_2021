# RRT(Rapidly Exploring Random Trees) Algorithm

RRT is a sampling based algortihm that solves one of the major issues with Dijkstra and A* Algorithms: The need of a graph to navigate upon.

RRT algorithm both creates a graph and finds the path

## Sampling Based Path Planning
A set of Random Nodes are slected from the free space to form the graph. This is map is called a Probabilistic RoadMap(PRM) because as the number of nodes goes to $\infty$, the probability that the PRM represents the actual free space goes to 1.  
### Pros 
1. The PRM captures the structure of the free space in way fewer nodes than with a grid graph

### Cons
1. Since the number of interations is finite, and the nodes are selected randomly, it is possible that the path found might not be the best one.

## RRT
The algorithm for RRT is as follows:  
1. Points are randomly generated and connected to the closest available nodes.
2. Each time a vertex is generated, a collision check is done with the obstacles 
3. When chaining a vertex with its neighbour, collision must be avoided
4. The algorithm ends when a node is generated within the goal region, or a limit is reached
5. 