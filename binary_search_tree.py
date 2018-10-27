from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root == None:
            return True
        return False

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return self._search(key,self.root)

    def _search(self, key, node):
        if key == node.key:
            return True
        elif key > node.key:
            if node.right == None:
                return False
            else:
                return self._search(key, node.right)
        elif key < node.key:
            if node.left == None:
                return False
            else:
                return self._search(key, node.left)

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        self._insert(key, data, self.root)

    def _insert(self, key, data, node):
        temp = TreeNode(key, data)
        if node == None:
            self.root = temp       
        elif temp.key == node.key:
            node.data = temp.data
        elif temp.key > node.key:
            if node.right == None:
                node.right = temp
            else:
                return self._insert(key, data, node.right)
        elif temp.key < node.key:
            if node.left == None:
                node.left = temp
            else:
                return self._insert(key, data, node.left)

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        if node.left == None:
            return node.key, node.data
        else:
            return self._find_min(node.left)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty():
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        if node.right == None:
            return node.key, node.data
        else:
            return self._find_max(node.right)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            return self._tree_height(self.root)
    
    def _tree_height(self, node):
        if node == None:
            return 0
        elif node == self.root:
            return max(self._tree_height(node.left),self._tree_height(node.right))
        else:
            return max(self._tree_height(node.left),self._tree_height(node.right)) + 1

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return self._inorder_list(self.root)

    def _inorder_list(self, node):
        returnlist = []
        if node.left == None and node.right == None:
            returnlist.extend([node.key])
        elif node.left == None and node.right != None:
            returnlist.extend([node.key]) 
            returnlist.extend(self._inorder_list(node.right))
        elif node.left != None and node.right == None:
            returnlist.extend(self._inorder_list(node.left))
            returnlist.extend([node.key])
        else:
            returnlist.extend(self._inorder_list(node.left))
            returnlist.extend([node.key])
            returnlist.extend(self._inorder_list(node.right))
        return returnlist 

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return self._preorder_list(self.root)

    def _preorder_list(self, node):
        returnlist = []
        if node.left == None and node.right == None:
            returnlist.extend([node.key])
        elif node.left == None and node.right != None:
            returnlist.extend([node.key]) 
            returnlist.extend(self._preorder_list(node.right))
        elif node.left != None and node.right == None:
            returnlist.extend([node.key])
            returnlist.extend(self._preorder_list(node.left))
        else:
            returnlist.extend([node.key])
            returnlist.extend(self._preorder_list(node.left))
            returnlist.extend(self._preorder_list(node.right))
        return returnlist 
        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!
        nodelist = []
        i = 0
        returnlist = []
        q.enqueue(self.root)
        while not q.is_empty():
            nodelist.append(q.dequeue())
            if nodelist[i].left != None:
                q.enqueue(nodelist[i].left) 
            if nodelist[i].right != None:
                q.enqueue(nodelist[i].right)
            i +=1
        for j in range(len(nodelist)):
            returnlist.append(nodelist[j].key)
        return returnlist 

        
