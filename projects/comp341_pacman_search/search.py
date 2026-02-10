













"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    
    frontier = util.Stack()
    
    start = problem.getStartState()
    frontier.push((start, []))
    
    visited = set()
    while not frontier.isEmpty():
        state, path = frontier.pop()
        
        if problem.isGoalState(state):
            return path
        if state in visited:
            
            continue
        visited.add(state)
        
        for succ, action, _ in problem.getSuccessors(state):
            if succ not in visited:
                
                frontier.push((succ, path + [action]))
    return [] 


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    start = problem.getStartState()
    frontier.push((start, []))  
    visited = set()  

    while not frontier.isEmpty():
        state,path = frontier.pop()
        
        if state in visited:
            continue
        visited.add(state)

        
        if problem.isGoalState(state):
            return path
        
        for next_state, action, cost in problem.getSuccessors(state):
            if next_state not in visited:
                
                new_path = path + [action]
                frontier.push((next_state, new_path))
    
    return []  



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    start = problem.getStartState()
    frontier.push((start, [], 0), 0)
    
    best_g = {start: 0}
    closed = set()
    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        
        if state in closed:
            continue
        closed.add(state)
        
        if problem.isGoalState(state):
            return path
        
        for succ, action, stepCost in problem.getSuccessors(state):
            new_g = g + stepCost
            
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                frontier.push((succ, path + [action], new_g), new_g)
    
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((start, [], 0), heuristic(start, problem))  

    
    best_g = {start: 0}
    
    closed = set()
    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        if state in closed:
            continue
        closed.add(state)

        if problem.isGoalState(state):
            return path
        
        for succ, action, stepCost in problem.getSuccessors(state):
            new_g = g + stepCost
            
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                f = new_g + heuristic(succ, problem)
                frontier.push((succ, path + [action], new_g), f)
    
    return []




bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
