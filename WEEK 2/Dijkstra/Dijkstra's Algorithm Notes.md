# Dijkstra's Algorithm Notes

Dijkstra’s Algorithm seeks to find the shortest path between two nodes in a graph with weighted edges.  

- **Single Source Shortest Path Algorithm**: Works for environments with only one source, where it can find the shortest possible path.  
- Works on both **Directed** and **Non-Directed** graphs

#

1. Dijkstra's Algorithm assumes that at the start, all other nodes except the source node are at an infinite distance from the source node (the source node is a t 0 distance since we are already there).
2. Next it finds all the nodes that have a direct connection to the source node. These nodes will have their distance equal to their edge weight.
3. Select the shortest path out of the source
4. On the shortest path, we perform an operation known as **Relaxation** on all nodes directly connected to the current node.   
Let us have a series of nodes s -> u -> v.  
Let c[u,v] represent the cost of an edge between u and v.  
Let d[u] represent distance of a node u from the source node s.  
***if( d[u] + c[u,v] < d[v] )  
d[v] = d[u] + c[u,v]***  
Thus, d[v] in this case is the indirect distance of v from s via u.

## Complexity
- Let the number of vertices be n.
- First the algorithm finds the vertex. NExt it finds all the vertices connected to that vertex. As a worst case senario, a vertice x will be connected to all n vertices be edges. So the worst case complexity will be n(to find a vertex) * n(to find the vertices connected to it) = n<sup>2</sup>

## Drawbacks
- Dijkstra's algorithm MAY not work on graphs whose edges have **Negative Weightages**.  



