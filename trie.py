# Trie data stucture
class Trie:
    def __init__(self):
        self.root = {'*': "*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] = {}
            curr_node = curr_node[letter]
        curr_node['*'] = '*'
    
    def check_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                return False
            curr_node = curr_node[letter]
        return '*' in curr_node