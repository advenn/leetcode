# # create BFS algorithm
# #
# # @param graph: dictionary of graph
# # @param start: start node
# # @param end: end node
# # @return: list of the shortest path
# def bfs(graph, start, end):
#     queue = [(start, [start])]
#     while queue:
#         (vertex, path) = queue.pop(0)
#         for next in graph[vertex] - set(path):
#             if next == end:
#                 yield path + [next]
#             else:
#                 queue.append((next, path + [next]))
#
#
# #
# # create graph
# #
#
# # Find the length of the shortest path
# # from “cab” to “bat”.
# graph = {
#     "cab": {"cat", "car"},
#     "car": {"bar", "cat"},
#     "bar": {"bat"},
#     "cat": {"bat", "mat"},
#     "mat": {"bat"},
#     "bat": set()
# }
#
#
#
#
#     # 'A': {'B', 'C', 'D'},
#     # 'B': {'A', 'D', 'E', 'F'},
#     # 'C': {'A', 'F', 'G', 'H'},
#     # 'D': {'B', 'E',},
#     # 'E': {'B', 'F',},
#     # 'F': {'C', 'E', },
#     # 'G': {'H',},
#     # 'H': {'G', },
# # }
# #
# # print shortest path
# #
# # print(list(bfs(graph, 'A', 'F')))
# #
# # print shortest path
# #
# print(list(bfs(graph, "cab", "bat")))

from collections import deque

graph = {}
graph['you'] = ['alice', 'bob' 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
print(graph)

search_queue = deque()
search_queue += graph['you']
