import queue

class Graph:
    def __init__(self, n):
        self.size = n
        self.vertex = {}
        for i in range(n):
            self.vertex[i] = []

    def connect(self, x, y):
        self.vertex[x].append(y)
        self.vertex[y].append(x)

    def find_all_distances(self, s):
        distances = [-1] * self.size
        distances[s] = 0

        next_to_visit = queue.Queue()
        next_to_visit.put(s)
        visited_vertex = {s}

        while not next_to_visit.empty():
            current = next_to_visit.get()

            for adj in self.vertex[current]:
                if adj not in visited_vertex:
                    distances[adj] = distances[current] + 6
                    visited_vertex.add(adj)
                    next_to_visit.put(adj)

        for i, d in enumerate(distances):
            if i != s:
                print("{} ".format(d), end='')

        print()
        return

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1)
    s = int(input())
    graph.find_all_distances(s-1)

