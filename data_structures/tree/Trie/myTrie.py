class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

    def __repr__(self):
        return str(self.children)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def __repr__(self):
        return str(self.root)

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

def deleteString(trie, word, index):
    ch = word[index]
    currentNode = trie.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            trie.children.pop(ch)
            return True

    if currentNode.endOfString == True:
        deleteString(currentNode, word, index + 1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisNodeBeDeleted == True:
        trie.children.pop(ch)
        return True
    else:
        return False

myTrie = Trie()
myTrie.insertString("API")
myTrie.insertString("APPLЕ")

deleteString(myTrie.root, 'API', 0)
print(myTrie)
