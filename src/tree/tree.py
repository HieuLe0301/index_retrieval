from node import Node

class Tree:
    def __init__(self, root):
        self.root = root

        
        active_nodes = []

        def 

        self.active_nodes = active_nodes

    def add_heading(self, heading):
        level = heading.get_level()

        self.active_nodes[level-1].chidren.append(heading)
        heading.parent = self.active_nodes[level-1]
        
        self.active_nodes[level] = heading
