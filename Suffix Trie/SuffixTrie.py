class SuffixTrie:
    def __init__(self,string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(n^2) time | O(n^2) space
    def populateSuffixTrieFrom(self,string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i,string)
    
    # O(m) time | O(1) space
    def insertSubstringStartingAt(self,i,string):
        node = self.root
        for j in range(i,len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        
        node[self.endSymbol] = True
    # O(m) time | O(1) space
    def contains(self,string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


# Time Complexity: O(n^2 + m) where n is the length of the input string and m is the length of the query string.
# Space Complexity: O(n^2) where n is the length of the input string.
# Test
#                                   R   o   o   t

#                             /           |            \
#                           b             a              c
#                         /   \           |              |
#                        a     c          b              *
#                       /      |          |
#                      b       *          c
#                     /                   |
#                    c                    *
#                   /                     |
#                  *                      *                          

string = "babc"
suffixTrie = SuffixTrie(string)
print(suffixTrie.contains("abc")) # True
print(suffixTrie.contains("ab")) # False
print(suffixTrie.contains("babc")) # True
print(suffixTrie.contains("bc")) # True
print(suffixTrie.contains("c")) # True
print(suffixTrie.contains("b")) # False
print(suffixTrie.contains("ba")) # False
print(suffixTrie.contains("bab")) # False
