class Node:
    def __init__(self):
        self.id = 0
        self.document_id = 0
        self.content = 0
        self.parent = None
        self.children = []

    def is_leaf(self):
        return len(self.children) == 0

    def get_level(self):
        if self.parent == None:
            return 0
        else:
            return self.parent.get_level() + 1

    def add_child(self, node):
        self.children.append(node)

    