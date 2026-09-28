#bfs --> queue method, fifo

from collections import deque #double ended queue

def bfs(root):
  queue = deque()

  if root:  # base case
    queue.append(root)

  level = 0
  while len(queue) > 0:
    print("level: ", level)
    for i in range(len(queue)):
      curr = queue.popleft()
      print(curr.val)
      if curr.left: #null checker
        queue.append(curr.left)
      if curr.right: #null checker
        queue.append(curr.right)
    level += 1 

