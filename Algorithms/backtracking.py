#back tracking basic algo

#determine if a path exists from root to leaf node, a zero in the way must not exist. 

def canReachLeaf(root, path):
  if not root or root.val == 0: #null or equal to 0
    return False
  path.append(root.val)

  #check for if left node / right node both not nulls
  if not root.left and not root.right:
    return True 

  #recurse left node
  if canReachLeaf(root.left, path):
    return True
  #recurse right node
  if canReachLeaf(root.right, path):
    return True
  path.pop()
  return False 
  

  
  
