
class BinarySearchTreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        
    def __str__(self):
        return str(self.key) + " " + str(self.value)
    
    def __repr__(self):
        return str(self.key) + " " + str(self.value)
    
    def __eq__(self, other):
        return self.key == other.key and self.value == other.value
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):
        return self.key < other.key
    
    def __gt__(self, other):
        return self.key > other.key
    
    def __le__(self, other):
        return self.key <= other.key
    
    def __ge__(self, other):
        return self.key >= other.key


class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def __str__(self):
        return str(self.root)
    
    def __repr__(self):
        return str(self.root)
    
    def __iter__(self):
        return BinarySearchTreeIterator(self.root)
    
    def __len__(self):
        return self.size(self.root)
    
    def __contains__(self, key):
        return self.get(key) is not None
    
    def size(self, node):
        if node is None:
            return 0
        return 1 + self.size(node.left_child) + self.size(node.right_child)
    
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left_child), self.height(node.right_child))
    
    def get(self, key):
        return self._get(self.root, key)
    
    def _get(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._get(node.left_child, key)
        return self._get(node.right_child, key)
    
    def put(self, key, value):
        self.root = self._put(self.root, key, value)
        
    def _put(self, node, key, value):
        if node is None:
            return BinarySearchTreeNode(key, value)
        if key == node.key:
            node.value = value
        elif key < node.key:
            node.left_child = self._put(node.left_child, key, value)
        else:
            node.right_child = self._put(node.right_child, key, value)
        return node
    
    def delete(self, key):
        self.root = self._delete(self.root, key)
        
    def _delete(self, node, key):
        if node is None:
            return None
        if key == node.key:
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            temp = node
            node = self._min(temp.right_child)
            node.right_child = self._delete_min(temp.right_child)
            node.left_child = temp.left_child
        elif key < node.key:
            node.left_child = self._delete(node.left_child, key)
        else:
            node.right_child = self._delete
            
            
    def delete_min(self):
        self.root = self._delete_min(self.root)
        
        
    def _delete_min(self, node):
        if node is None:
            return None
        if node.left_child is None:
            return node.right_child
        node.left_child = self._delete_min(node.left_child)
        return node
    
    
    
    def min(self):
        return self._min(self.root)
    
    def _min(self, node):
        if node is None:
            return None
        if node.left_child is None:
            return node
        return self._min(node.left_child)
    
    def max(self):
        return self._max(self.root)
    
    def _max(self, node):
        if node is None:
            return None
        if node.right_child is None:
            return node
        return self._max(node.right_child)
    
    def floor(self, key):
        node = self._floor(self.root, key)
        if node is None:
            return None
        return node.key
    
    def _floor(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left_child, key)
        temp = self._floor(node.right_child, key)
        if temp is not None:
            return temp
        return node
    

class BinarySearchTreeIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
        
    def __next__(self):
        if len(self.stack) == 0:
            raise StopIteration()
        node = self.stack.pop()
        self._push_left(node.right_child)
        return node
    
    def _push_left(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left_child
            
    def __iter__(self):
        return self
    