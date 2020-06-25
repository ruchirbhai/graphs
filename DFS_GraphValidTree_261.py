# Given n nodes labeled from 0 to n-1 and a list of undirected edges 
# (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

# Example 1:

# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
# Example 2:

# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
# Note: you can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.

# Notes
# A valid Tree is a connected graph with no cycles
# A tree doesnt necessarily mean a rooted tree

class Solution:
    def valid_tree_dfs(self, n, edges):
        # PART 1: BUILD A GRAPH
        # here we will create a parent array also to keep track of parent array

        # Create adj_list of length n using comprehension
        adj_list = [[] for _ in range(n)]
        # create a visited array
        visited = [-1] * n
        # Create a parent array
        parent = [-1] * n
        # populate the adj_list with the values in the array in taking advantage of convinient indices
        for (src, dst) in edges:
            adj_list[src].append(dst)
            adj_list[dst].append(src)
        
        # PART 2: DFS/ BFS loop
        # Here we need to add a check for cycles We check this by 
        # looking for the fact that the neighbor is not a parent of the node return true
        def dfs(source):
            # change the visited status as soon as you reach the node
            visited[source] = 1

            for neighbor in adj_list[source]:
                # if neighbor is not visited then update its parent and loop in futher
                if visited[neighbor] == -1:
                    # update parent information
                    parent[neighbor] = source
                    # call dfs on the neighbor
                    if dfs(neighbor):
                        return True
                else:
                    # if the neighbor has already been visited then
                    if parent[source] != neighbor:
                        # we catch a cycle??
                        return True

        # PART 3: OUTER LOOP
        # Here we need to ensure two things the value of components should not be > 1
        # and bfs/DFS detects a cycle and it retutns false
        # our return should check if compnents is > 1 or bfs/dfs is false we return false else true

        # initialize component counter to 0
        components = 0

        # Iterate over the lenght of entire array
        for v in range(n):
            if visited[v] == -1:
                components += 1
                if components > 1:
                    return False
                if dfs(v):
                    return False
        
        return True
                    


if __name__ == "__main__":
    n = 5
    # edges = [[0,1], [0,2], [0,3], [1,4]]
    edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    obj = Solution()
    print(obj.valid_tree_dfs(n,edges))
    