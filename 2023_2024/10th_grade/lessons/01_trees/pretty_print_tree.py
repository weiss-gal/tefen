class Node:
    def __init__(self, word):
        self.word = word
        self.upper = None
        self.lower = None

    def get_upper(self):
        return self.upper

    def get_lower(self):
        return self.lower

def pretty_print(tree, depth=0):
    if tree is None:
        return

    pretty_print(tree.get_upper, depth+2)
    print("  " * depth + tree.word)
    pretty_print(tree.get_lower, depth+2)

root = 
