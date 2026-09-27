#bst binary search tree --> binary trees that are sorted property 

#ver1: left child always smaller, right child always greater than parent
#if sorted -> O(logn) time !! only when roughly balanced 

def search(root, target):
  if not root: #null and search ran out of targets
    return False

  if target > root.val: #greater = right side search
    return search(root.right, target)
  elif target < root.val: #less = left side search
    return search(root.left, target)
  else: # equal to target --> return value --> kinda like binary search 
    return True   

#bst insert

def insert(root, val):
  if not root: #if not null
     return TreeNode(val)
  if val > root.val:
    root.right = insert(root.right, val)
  elif val < root.val:
    root.left = insert(root.left, val)
  return root

#bst remove --> need to find minimum, leftmost

def minValNode(root):
  curr = root
  while curr and curr.left:
    curr = curr.left
  return curr

def remove(root, val):
  if not root:
    return None
#case 1: 0 or 1 children
  if val > root.val:
    root.right = remove(root.right, val)
  elif val < root.val:
    root.left = remove(root.left, val)
  else: #case 2: 2 children
    if not root.left: #is left node missing / left node = null
      return root.right
    if not root.right:
      return root.left
    else:
      minNode = minValNode(root.right)
      root.val = minNode.val
      root.right = remove(root.right, minNode.val)
  return root 
    


