#3 methods of dfs in trees: inorder, preorder, postorder

#1. inorder
def inorder(root):
  if not root: #null we can just return
    return
  inorder(root.left) #traverse left the print
  print(root.val)
  inorder(root.right)

#2. preorder  
def preorder(root):
  if not root:
    return
  print(root.val) #print before we proder
  preorder(root.left)
  preorder(root.right) 

#3. postorder
def postorder(root):
  if not root:
    return
  postorder(root.left) #traverse all left
  postorder(root.right) #traverse all right
  print(root.val) #then print out values


