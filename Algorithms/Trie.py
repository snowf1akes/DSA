#Trie or Prefix Tree
class TrieNode:
  def __init__(self):
    self.children = {} #empty hashmap
    self.word = False #boolean that determines if end of word or not

class Trie:
  def __init__(self):
    self.root = TrieNode()  
  
  def insert(self, word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        curr.children[c] = TrieNode()
      curr = curr.children[c]
    curr.word = True

  def search(self,word):
    curr = self.root
    for c in word:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return curr.word #last index, so word exists inside hashmap 

  def startsWith(self,prefix):
    curr = self.root 
    for c in prefix:
      if c not in curr.children:
        return False
      curr = curr.children[c]
    return True


