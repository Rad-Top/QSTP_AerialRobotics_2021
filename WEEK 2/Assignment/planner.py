# This is not a complete program, you have to fill these to complete the search.
from GridWorld import GridWorld, Node

class Planner:
    def __init__(self, env):
        """
        Args:
            1. env: GridWorld. This constructs the environment and provides requisite collision checking functionalities.
        """
        self.env = env
        # Take in more arguments if required.

    def search(self, start, goal):
        # Given a start and goal location, perform search using A-star or Dijkstra

        return path

if __name__ == "__main__":
    env = GridWorld()
    planner = Planner(env)