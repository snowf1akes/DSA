#Binary trees basics first 

class TreeNode {
    int val;
    TreeNode left = null;
    TreeNode right = null;

    TreeNode(int val) {
        this.val = val;
    }
}

#BST Traversal
    #recursive function that searches for smallest value in left subtree
    #parent, left subtree, check children for smaller one, then recursively repeat until base case (null) 
    #go back to parent, check right subtrees, 
    #inorder code: left, root, right
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        print(root.val)
        inorder(root.right)

    #time complexity --> size of tree O(n) --> traversing sorted array 
    #if given arrays to build bst, insertion inside for trees = O(n + nlogn), since we only care about largest variable --> its O(nlogn)
    
    #preorder code: root, left, right
    def preorder(root):
        if not root:
            return
        print(root.val)
        preorder(root.left)
        preorder(root.right)
    #post order code: left, right, root
    def postorder(root):
        if not root:
            return
        postorder(root.left)
        postorder(root.right)
        print(root.val)

    #reverse order code: right, root, left

    def reverseorder(root):
        if not root: 
            return
        reverseorder(root.right)
        print(root.val)
        reverseorder(root.left)

#depth first search: !! DFS !!
#go as deep first, then do the rest of the nodes, the above are all examples of DFS
#if bfs, its layer by layer, kinda like heaps with its structure. 




