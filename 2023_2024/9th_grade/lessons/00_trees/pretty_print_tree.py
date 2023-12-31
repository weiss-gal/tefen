# use this function to pretty print the tree
# it requries that you implement the following keys:
#   - 'yes'
#   - 'no'
#   - 'question'
def pretty_print(tree, depth=0):
    if tree is None:
        return

    pretty_print(tree.get('yes'), depth+1)
    print("  " * depth + tree.get('question')
    pretty_print(tree.get('no'), depth+1)

words = [
    'ocean', 'print', 'window', 'apple', 'rabbit', 'pizza', 'music', 'happy', 'dance', 'coffee',
    'planet', 'flower', 'space', 'jungle', 'magic', 'frozen', 'melon', 'tiger', 'lemon', 'island',
    'hello', 'purple', 'cookie', 'garden', 'piano', 'shadow', 'zebra', 'sunset', 'whale', 'forest',
    'orange', 'river', 'unicorn', 'smile', 'butter', 'mirror', 'castle', 'flamingo', 'echo', 'mango',
    'diamond', 'soccer', 'rainbow', 'silent', 'penguin', 'breeze', 'robot', 'crystal', 'basket', 'tornado'
]

# TODO: create a tree with the words above
root = None 

pretty_print(root)
