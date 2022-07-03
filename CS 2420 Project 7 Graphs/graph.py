import math


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = {}

    def add_vertex(self, label):
        if not isinstance(label, str):
            raise ValueError("Vertex must be a string.")
        self.vertices.append(label)
        self.edges[label] = {}
        return self

    def add_edge(self, src, dest, weight):
        if src not in self.vertices or dest not in self.vertices:
            raise ValueError("Source or destination vertices do not exist.")
        weight = float(weight)
        self.edges[src][dest] = weight
        return self

    def get_weight(self, src, dest):
        try:
            for key, value in self.edges[src].items():
                if key == dest:
                    return value
        except ValueError:
            pass
        return math.inf

    def dfs(self, starting_vertex):
        if starting_vertex not in self.vertices:
            raise ValueError("Specified starting vertex does not exist")
        visited_nodes = []
        self.dfs2(starting_vertex, visited_nodes)
        yield from visited_nodes

    def dfs2(self, vertex, visited):
        if vertex not in visited:
            visited.append(vertex)
            for i in self.edges[vertex]:
                self.dfs2(i, visited)

    def bfs(self, starting_vertex):
        if starting_vertex not in self.vertices:
            raise ValueError("Specified starting vertex does not exist")
        visited_nodes = [starting_vertex]
        to_visit = []
        for i in self.edges[starting_vertex]:
            visited_nodes.append(i)
            to_visit.append(i)
        while len(to_visit) != 0:
            self.bfs2(to_visit.pop(0), visited_nodes, to_visit)
        yield from visited_nodes

    def bfs2(self, node, visited, to_visit):
        for i in self.edges[node]:
            if i not in visited:
                visited.append(i)
                to_visit.append(i)

    def dsp(self, src, dest):
        if src == dest:
            return 0, [src]
        shortest = {}
        for i in self.vertices:
            shortest[i] = [math.inf, ""]
        shortest[src] = [0.0, src]
        for i in self.vertices:
            self.visit_children(i, shortest)
        try:
            path = (int(shortest[dest][0]), [src, dest])
        except OverflowError:
            return math.inf, []
        curr = shortest[dest][1]
        while curr != src:
            path[1].insert(1, curr)
            curr = shortest[curr][1]
        return path

    def visit_children(self, node, shortest):
        for i in self.edges[node]:
            if shortest[node][0] + self.edges[node][i] < shortest[i][0]:
                shortest[i] = [shortest[node][0] + self.edges[node][i], node]

    def dsp_all(self, src):
        out = {}
        for i in self.vertices:
            out[i] = self.dsp(src, i)[1]
        return out

    def __str__(self):
        out = "digraph G {\n"
        for key, value in self.edges.items():
            for i, j in value.items():
                out += f"   {key} -> {i} [label=\"{j}\",weight=\"{j}\"];\n"
        out += "}\n"
        return out


def main():
    graph = Graph()
    vertices = (chr(x) for x in range(65, 71))
    for i in vertices:
        graph.add_vertex(i)
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "F", 9)
    graph.add_edge("B", "C", 8)
    graph.add_edge("B", "D", 15)
    graph.add_edge("B", "F", 6)
    graph.add_edge("C", "D", 1)
    graph.add_edge("E", "C", 7)
    graph.add_edge("E", "D", 3)
    graph.add_edge("F", "B", 6)
    graph.add_edge("F", "E", 3)
    print(graph)

    print("starting DFS with vertex A")
    for i in graph.dfs("A"):
        print(i, end="")
    print()

    print("starting BFS with vertex A")
    for i in graph.bfs("A"):
        print(i, end="")
    print()

    print(graph.dsp("A", "F"))
    print(graph.dsp("A", "A"))
    print(graph.dsp_all("A"))


if __name__ == '__main__':
    main()
