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

class Solution:
    def is_graph_bipartite(self, graph):
        # Part 1: create the adj_list which is already provided as input
        adj_list = graph
        n = len(graph)
        # create the visited, parent and distance lists
        visited = [-1] * n
        parent = [-1] * n
        color = [-1] * n

        # Part 2: Call BFS to traverse the graph
        def dfs(source):
            # As soon as we call bfs we update the source visited 
            visited[source] = 1
            # Change the color as level changes
            if parent[source] == -1:
                color[source] = 0
            else:
                color[source] = 1 - color[parent[source]]

            for neighbor in adj_list[source]:
                if visited[neighbor] == -1:
                    # Who is your daddy
                    parent[neighbor] = source
                    # Do the recursion
                    if dfs(neighbor) == False:
                        return False
                else:
                    if color[source] == color[neighbor]:
                        # It means that the cycle end on a even number thus the tree is not bipartate
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
                
                if dfs(v) == False:     # Even if single bfs returns false we need to return false oveall
                    return False        
        return True

if __name__ == "__main__":
    # Graph for the false case
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    # # Graph for the True case
    # graph = [[1,3], [0,2], [1,3], [0,2]]

    obj = Solution()
    print(obj.is_graph_bipartite(graph))
