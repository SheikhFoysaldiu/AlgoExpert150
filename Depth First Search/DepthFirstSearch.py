class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


# Test
# Create a graph
#           A
#         / | \
#        B  C  D
#       / \    / \
#      E   F  G   H
#         / \    /
#        I   J  K


# Time Complexity: O(v + e) where v is the number of vertices and e is the number of edges in the graph.
# Space Complexity: O(v) where v is the number of vertices in the graph.
dfs = Node("A")
dfs.addChild("B").addChild("C").addChild("D")
dfs.children[0].addChild("E").addChild("F")
dfs.children[2].addChild("G").addChild("H")
dfs.children[0].children[1].addChild("I").addChild("J")
dfs.children[2].children[0].addChild("K")

print(dfs.depthFirstSearch([]))

# Output: ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
