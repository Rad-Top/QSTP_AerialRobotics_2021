
# Path Planning Components
Identifying a trajectory to move a robot to a gaol.

Two Approaches:

- Graph search methods  
Graph refers to a collection of nodes and connecting edges  

- Potential Field Planning  
Both of these assume we have a map of the environment and thus we know where we are and where we want to be.

For the graph search method, there are 2 important concepts  

- Graph Construction  

- Graph Search Algorithms  

Path planning approaches are usually gauged by 2 factors:  
- Completeness: Whether the robot will reach the required point  

- Optimaltiy: Whether the approach will find the bet solution (Best could be in terms of, least distance travelled, least amount of resources used, etc.)

## Graph Search Methods

### Visibility Graph

In a 2D space, the vertices of the obstacles are joined with other vertices in the line of sight.  

#### Pros:

- Finds the optimal path (shortest)
- Is a Complete Method (If a solution exists, this method is guarenteed to find it)

#### Cons:

- Becomes Costly in vertex rich environments
- Dangerous because the robot goes pretty close to the objects, thus increasing the possibility of collisions

    -   One way to fix this is to inflate the objects before making the graph so that the robot isn't as close to the objects.

### Voronoi Diagram

Creates lines which are equidistanct from all the objects and these lines form the paths.

#### Pros

- Maximizes the distance between the robot and the objects
- Is a Complete Method (If a solution exists, this method is guarenteed to find it)
- Easy to execute. As long as the sensor can find the objects, the robot just turns to keep itself equidistant from them
- It can automatically map the environment. If the robot is set loose in an environment, it can easily generate the map for that environment using this method. 

#### Cons:

- Paths are usually not the shortest possible paths
- Has problems with short range sensors

### Fixed Cell Decomposition Method

A grid with fixed cells is overlayed on the map. If any cell has any part of the obstacle in it, it s considered to be filled  
If a cell has nothing in it, it is marked as empty.  

#### Pros:

- Yields relatively simple path planning
- Good for map generation with range finding sensor

## Potential Field Mapping  

Objective is to create a gradient "U" around the objects.  
This directs the robot towards the goal and away from the objects.    

Robot behaves as a ball acted upon by a force F = -$\triangledown$ *U*(x,y)

- Serves as a both path planning and a control law
- *U* can be treated as a sum of an attractive and a repulsive potential
- Attractive Potential goes to 0 at goal.
- Repulsive Potential is high at objects and 0 elsewhere


## Discretization of Configuration Space

The Configuration Space (Set of all **Possible** configurations of the robot) often needs to be discretized to make path planning algorithms work on it.
- Combinatorial Planning  
    Takes all possible states of the robot and discretizes them into smaller states, similiar to a grid style representation. A problem with this method is, as the dimensionality of the robot(the number of joints or degrees of freedom) increases, the amount of discretisation increases exponentially and results in large calculations
- Sampling Based Planning  
    Uses collision detection to probe and incrementally search the C-space for a solution
