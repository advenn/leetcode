# # Python program for Dijkstra's single
# # source shortest path algorithm. The program is
# # for adjacency matrix representation of the graph
# class Graph:
#     def __init__(self, vertices):
#         self.V = vertices
#         self.graph = [[0 for column in range(vertices)]
#                       for row in range(vertices)]
#
#     def printSolution(self, dist):
#         print("Vertex \t Distance from Source")
#         for node in range(self.V):
#             print(node, "\t\t", dist[node])
#
#     # A utility function to find the vertex with
#     # minimum distance value, from the set of vertices
#     # not yet included in shortest path tree
#     def minDistance(self, dist, sptSet):
#
#         # Initialize minimum distance for next node
#         min = 1e7
#
#         # Search not nearest vertex not in the
#         # shortest path tree
#         for v in range(self.V):
#             if dist[v] < min and sptSet[v] == False:
#                 min = dist[v]
#                 min_index = v
#
#         return min_index
#
#     # Function that implements Dijkstra's single source
#     # shortest path algorithm for a graph represented
#     # using adjacency matrix representation
#     def dijkstra(self, src):
#
#         dist = [1e7] * self.V
#         dist[src] = 0
#         sptSet = [False] * self.V
#
#         for cout in range(self.V):
#             print(dist, sptSet, cout, self.V)
#             # Pick the minimum distance vertex from
#             # the set of vertices not yet processed.
#             # u is always equal to src in first iteration
#             u = self.minDistance(dist, sptSet)
#
#             # Put the minimum distance vertex in the
#             # shortest path tree
#             sptSet[u] = True
#
#             # Update dist value of the adjacent vertices
#             # of the picked vertex only if the current
#             # distance is greater than new distance and
#             # the vertex in not in the shortest path tree
#             for v in range(self.V):
#                 if (self.graph[u][v] > 0 and
#                         sptSet[v] == False and
#                         dist[v] > dist[u] + self.graph[u][v]):
#                     dist[v] = dist[u] + self.graph[u][v]
#
#         self.printSolution(dist)
#
#
# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#            [4, 0, 8, 0, 0, 0, 0, 11, 0],
#            [0, 8, 0, 7, 0, 4, 0, 0, 2],
#            [0, 0, 7, 0, 9, 14, 0, 0, 0],
#            [0, 0, 0, 9, 0, 10, 0, 0, 0],
#            [0, 0, 4, 14, 10, 0, 2, 0, 0],
#            [0, 0, 0, 0, 0, 2, 0, 1, 6],
#            [8, 11, 0, 0, 0, 0, 1, 0, 7],
#            [0, 0, 2, 0, 0, 0, 6, 7, 0]
#            ]
# print(g.graph)
# g.dijkstra(0)
#
# # This code is contributed by Divyanshu Mehta

graph = {
    'a': {'b': 1, 'c': 1.5, 'e': 2},
    'b': {'d': 1.5},
    'c': {'l': 2, 'e': 1.5}, 'd': {'f': 1},
    'e': {'g': 2, "h": 2, "k": 1, "l": 2},
    'f': {'g': 1},
    'g': {'h': 1},
    'h': {'i': 1.5},
    'i': {'j': 2},
    'j': {},
    'k': {'i': 2, "h": 2}, 'l': {'k': 3}
}


def dijkstra(graph, start, end):
    shortest_distance = {}
    track_predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    track_path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                track_predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = end

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    track_path.insert(0, start)
    if shortest_distance[end] != infinity:
        print('Shortest distance is ' + str(shortest_distance[end]))
        print('And the path is ' + str(track_path))

dijkstra(graph, 'a', 'j')