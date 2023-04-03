class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if not node:
                node = TrieNode()  # similar to currentNode.children[ch] = node
                currentNode.children.update({ch: node})  # this way u can insert multiple kvps at once
            currentNode = node
        currentNode.endOfString = True
        print("Successfully inserted")

    def searchString(self, word):
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if not node:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        return False  # the case search(Ap) in App


myTrie = Trie()
myTrie.insertString("App")
myTrie.insertString("Appl")
print(myTrie.searchString('Ap'))  # False
