class Node:
    def __init__(self, word):
        self.word = word
        self.upper = None
        self.lower = None

    def get_upper(self):
        return self.upper

    def get_lower(self):
        return self.lower
    
    def set_upper(self, upper):
        self.upper = upper

    def set_lower(self, lower):
        self.lower = lower

    def __str__(self):
        return self.word
    
    def add(self, word):
        if word < self.word:
            if self.upper is None:
                self.upper = Node(word)
            else:
                self.upper.add(word)
        else:
            if self.lower is None:
                self.lower = Node(word)
            else:
                self.lower.add(word)

    def get_word(self):
        return self.word