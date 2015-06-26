import sys
import collections

class Element(object):
    WALL = 1
    HOLE = 2
    FLOOR = 3

CHAR_TO_ELEMENT_ENUM = {
    '*': Element.WALL,
    'o': Element.HOLE,
    ' ': Element.FLOOR
}

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = collections.defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance=1):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance

def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}
  nodes = set(graph.nodes)
  while nodes:
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node
    if min_node is None:
      break
    nodes.remove(min_node)
    current_weight = visited[min_node]
    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node
  return visited

class Point(object):
    def __init__(self, level, row, col):
        self.level = level
        self.row = row
        self.col = col

    def adjacent_to(self, point):
        return abs(self.level-point.level) + abs(self.row-point.row) + abs(self.col-point.col) == 1

    @property
    def adjacent_points(self):
        return [
            Point(self.level-1, self.row,   self.col),
            Point(self.level+1, self.row,   self.col),
            Point(self.level,   self.row-1, self.col),
            Point(self.level,   self.row+1, self.col),
            Point(self.level,   self.row,   self.col-1),
            Point(self.level,   self.row,   self.col+1)
        ]

    def __eq__(self, other):
        return self.level == other.level and self.row == other.row and self.col == other.col

    def __str__(self):
        return "(%i,%i,%i)" % (self.level, self.row, self.col)

    def __key(self):
        return self.level, self.row, self.col

    def __hash__(self):
        return hash(self.__key())

class Cube(object):
    def __init__(self, levels):
        self.levels = levels

    @property
    def length(self):
        return len(self.levels)

    def __str__(self):
        result = []
        counter = 0
        for level in self.levels:
            result.append("Level %i" % counter)
            counter += 1
            for row in level: result.append(''.join(row))
            result.append("")
        return "\n".join(result).strip()

    def _find_empty_cell_in_border(self, level):
        # Top row.
        for i in range(0, self.length):
            if self.levels[level][0][i] == ' ': return Point(level, 0, i)
        # Bottom row.
        for i in range(0, self.length):
            if self.levels[level][self.length-1][i] == ' ': return Point(level, self.length-1, i)
        # Sides.
        for i in range(1, self.length-1):
            if self.levels[level][i][0] == ' ': return Point(level, i, 0)
            if self.levels[level][i][self.length-1] == ' ': return Point(level, i, self.length-1)
        # Should never reach here if there is an empty cell in the border.
        return None

    @property
    def entrance(self):
        return self._find_empty_cell_in_border(0)

    @property
    def exit(self):
        return self._find_empty_cell_in_border(self.length-1)

    def _element(self, point):
        if point.level < 0 or point.row < 0 or point.col < 0 or \
                point.level >= self.length or point.row >= self.length or point.col >= self.length:
            return Element.WALL
        return CHAR_TO_ELEMENT_ENUM[self.levels[point.level][point.row][point.col]]

    def _can_travel(self, point_from, point_to):
        # Precondition.
        if self._element(point_from) == Element.WALL or self._element(point_to) == Element.WALL:
            return False

        # Adjacency.
        if not point_from.adjacent_to(point_to):
            return False

        # Various semantic cases, depending on levels.
        if point_from.level == point_to.level:
            return True
        elif point_from.level == point_to.level + 1:
            # "from" is one level above "to", i.e. we are moving down.
            return self._element(point_from) == Element.HOLE
        elif point_from.level + 1 == point_to.level:
            # "from" is one level below "to", i.e. we are moving up.
            return self._element(point_to) == Element.HOLE
        else:
            return False

    def _create_graph(self, visited, graph, current):
        if visited[(current.level, current.row, current.col)]: return
        visited[(current.level, current.row, current.col)] = True
        graph.add_node(current)
        for p in current.adjacent_points:
            if self._can_travel(current, p):
                graph.add_node(p)
                graph.add_edge(current, p)
                self._create_graph(visited, graph, p)
        return graph

    def graph(self):
        visited = collections.defaultdict(lambda: False)
        graph = Graph()
        self._create_graph(visited, graph, self.entrance)
        return graph

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0: continue
        length = int(test.split(';')[0])
        levels = list(zip(*[iter(zip(*[iter(test.split(';')[1])]*length))]*length))
        cube = Cube(levels)

        result = dijsktra(cube.graph(), cube.entrance)
        if cube.exit not in result:
            print(0)
        else:
            print(1 + result[cube.exit])

    test_cases.close()

if __name__ == '__main__':
    main()
