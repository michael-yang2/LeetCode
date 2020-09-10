class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['$'] = {}
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def recur(word, trie):
            if not word:
                if '$' in trie:
                    return True
                return False
            if word[0] in trie:
                return recur(word[1:], trie[word[0]])
            elif word[0] == '.':
                to_return = False
                for char in trie.keys():
                    to_return = to_return or recur(word[1:], trie[char])
                return to_return
            return False
        return recur(word, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)