import random

class Node:
    print("Not implemented yet")

# use this function to pretty print the tree
# it requries that you implement the following methods:
#   - get_upper()
#   - get_lower()
#   - get_word()
def pretty_print(tree, depth=0):
    if tree is None:
        return

    pretty_print(tree.get_upper(), depth+1)
    print("  " * depth + tree.get_word())
    pretty_print(tree.get_lower(), depth+1)

words = [
    'ocean', 'print', 'window', 'apple', 'rabbit', 'pizza', 'music', 'happy', 'dance', 'coffee',
    'planet', 'flower', 'space', 'jungle', 'magic', 'frozen', 'melon', 'tiger', 'lemon', 'island',
    'hello', 'purple', 'cookie', 'garden', 'piano', 'shadow', 'zebra', 'sunset', 'whale', 'forest',
    'orange', 'river', 'unicorn', 'smile', 'butter', 'mirror', 'castle', 'flamingo', 'echo', 'mango',
    'diamond', 'soccer', 'rainbow', 'silent', 'penguin', 'breeze', 'robot', 'crystal', 'basket', 'tornado'
]


pretty_print(root)
