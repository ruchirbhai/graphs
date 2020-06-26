# https://leetcode.com/problems/is-graph-bipartite/

# Given an undirected graph, return true if and only if it is bipartite.
# Recall that a graph is bipartite if we can split it's set of nodes into two 
# independent subsets A and B such that every edge in the graph has one node in A and another node in B.

# The graph is given in the following form: 
# graph[i] is a list of indexes j for which the edge between nodes i and j exists.  
# Each node is an integer between 0 and graph.length - 1.  
# There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

# Example 1:
# Input: [[1,3], [0,2], [1,3], [0,2]]
# Output: true
# Explanation: 
# The graph looks like this:
# 0----1
# |    |
# |    |
# 3----2
# We can divide the vertices into two groups: {0, 2} and {1, 3}.

# Example 2:
# Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
# Output: false
# Explanation: 
# The graph looks like this:
# 0----1
# | \  |
# |  \ |
# 3----2
# We cannot find a way to divide the set of nodes into two independent subsets.

# Note:
# graph will have length in range [1, 100].
# graph[i] will contain integers in range [0, graph.length - 1].
# graph[i] will not contain i or duplicate values.
# The graph is undirected: if any element j is in graph[i], then i will be in graph[j].

# Notes: For a graph to be birpartite we have to look at the following: 
#   If the graph is a tree then its always bipartite
#   If the graph is not a tree and has cycles we need to detect the cycle and do the foll: 
#       If the cycle has odd nodes then --> the graph is NOT bipartite
#       If the cycle has even nodes then --> the graph is bipartite

from collections import deque

class Solution:
    def is_graph_bipartite(self, graph):
        # Part 1: create the adj_list which is already provided as input
        adj_list = graph
        n = len(graph)
        # create the visited, parent and distance lists
        visited = [-1] * n
        parent = [-1] * n
        distance = [-1] * n

        # Part 2: Call BFS to traverse the graph
        def bfs(source):
            # As soon as we call bfs we update the source visited 
            visited[source] = 1
            # make a queue for the bfs
            q = deque([source])
            # Initialize the distance for the root 
            distance[source] = 0

            while len(q) != 0:
                # get the first element in the queue
                node = q.popleft()
                # iterate over the neighbours of the node
                for neighbor in adj_list[node]:
                    if visited[neighbor] == -1:
                        # for nodes not visited previously toggle to 1 as they have now been visited
                        visited[neighbor] =1
                        # Who is your daddy
                        parent[neighbor] = node
                        # append the neighbours for the next iteration of the while loop
                        q.append(neighbor)
                        # increment the distance wrt the root node
                        distance[neighbor] = distance[node] + 1
                    else:
                        if parent[node] != neighbor:
                            # for the above condition to be true it means we are inside a graph cycle
                            if distance[node] == distance[neighbor]:
                                # It means that the cycle is odd length thus the graph will not be bipartite
                                return False

            return True     # if no false reported so far then the subtree is bipartite  

        # Part 3: Outer Loop
        # We need to check if the graph is a valid tree
        components = 0

        for v in range(n):
            if visited[v] == -1:
                # increment the component
                components += 1
                # This check of greater than 1 is optional in this case
                if components > 1:
                    return False
                
                if bfs(v) == False:     # Even if single bfs returns false we need to return false oveall
                    return False        
        return True

if __name__ == "__main__":
    # # Graph for the false case
    # graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    # Graph for the True case
    graph = [[1,3], [0,2], [1,3], [0,2]]

    obj = Solution()
    print(obj.is_graph_bipartite(graph))
