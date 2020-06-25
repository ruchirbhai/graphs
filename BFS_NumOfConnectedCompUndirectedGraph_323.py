# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# write a function to find the number of connected components in an undirected graph.
# Example 1:
#      0          3
#      |          |
#      1 --- 2    4
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

# Example 2:
#      0           4
#      |           |
#      1 --- 2 --- 3
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# Note:
# You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] 
# is the same as [1, 0] and thus will not appear together in edges.

# Notes 
# this is an explicit graps problem
# DFS can be used here and also BFS can be used here
# union find comes into play only if you are required to process the edges in a particular order

# part 1: build the graph(adjecentList or Maps)
# Part 2: Use BFS or DFS Time Complexity for both is O(n+m) where is the m is the degree if the node
# for tress m was always equal to n-1
# Part 3: Outer Loop (Explore the whole graph)

# Build graph
# n = Num of vertices with their ids (convinient: 0 ... n-1)
# create adj_list = a 1D array of side n, initialized to an empty array/list
# "edges" - a list of edges(u,v)
# for (src, dst) in edges: 
#       adj_list[src].append(dst)
#       adj_list[dst].append(src)

from collections import deque

class Solution:
    def count_components(self, n, edges):
        # create empty adj_list of list 
        adj_list = [[] for _ in range(n)]
        # Create the adj_list by using the property of convinient indices and values being the same
        for (src, dst) in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        # initialize the visited array was -1 for length of n
        visited = [-1] * n

        def bfs(source):
            # source value being changed to 1 to ack the visitation
            visited[source] = 1

            q = deque([source])
            
            while len(q) != 0:
                node = q.popleft()
                for neighbor in adj_list[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.append(neighbor)
        
        # initialize component counter
        components = 0
        # iterate over entire arrary
        for v in range(n):
            # if the source has not been visited then increment by 1 and call dfs
            if visited[v] == -1:
                components +=1
                bfs(v)
        
        return components


# Use BFS
# we will need to call the BFS call multiple times
#   create a new queue and essentially use it a a visited array
# function bfs(source):
#   q = new Queue()
#   q.push(source)
#   visited[source] = 1
#   while q is not empty:
#       
if __name__ == "__main__":
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    obj = Solution()
    print(obj.count_components(n,edges))
    