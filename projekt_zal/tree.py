class Node:
    def __init__(self, parent=None, left=None, right=None, name=None, number=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.name = name
        self.number = number

class Tree:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)

    def getNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node