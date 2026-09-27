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
