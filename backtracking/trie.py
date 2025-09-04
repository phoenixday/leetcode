class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False


    def insert(self, word: str) -> None:
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.is_word = True


    def search(self, word: str) -> bool:
        node = self
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.is_word


    def startsWith(self, prefix: str) -> bool:
        node = self
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
