RED = 1
BLACK = 0


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.color = RED
        self.size = 1

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left = self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right = self.right.insert(key)
        else:
            self.key = key

        if self.right is not None and self.right.is_red() and not self.left.is_red():
            self = self.rotate_left()
        if (
            self.left is not None
            and self.left.is_red()
            and self.left.left is not None
            and self.left.left.is_red()
        ):
            self = self.rotate_right()
        if (
            self.left is not None
            and self.left.is_red()
            and self.right is not None
            and self.right.is_red()
        ):
            self.flip_colors()

        self.size = 1 + self.left_size() + self.right_size()
        return self

    def search(self, key):
        if key < self.key:
            if self.left is None:
                return None
            else:
                return self.left.search(key)
        elif key > self.key:
            if self.right is None:
                return None
            else:
                return self.right.search(key)
        else:
            return self

    def delete(self, key):
        if key < self.key:
            if self.left is not None:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right is not None:
                self.right = self.right.delete(key)
        else:
            if self.right is None:
                return self.left
            else:
                x = self.right.min()
                self.key = x.key
                self.right = self.right.delete_min()
                self.left = x.left
        self.size = 1 + self.left_size() + self.right_size()
        return self

    def min(self):
        if self.left is None:
            return self
        else:
            return self.left.min()

    def delete_min(self):
        if self.left is None:
            return self.right
        else:
            self.left = self.left.delete_min()
            self.size = 1 + self.left_size() + self.right_size()


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self.root.insert(key)
        self.root.color = BLACK

    def search(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)

    def delete(self, key):
        if self.root is not None:
            self.root = self.root.delete(key)
            if self.root is not None:
                self.root.color = BLACK

    def min(self):
        if self.root is None:
            return None
        else:
            return self.root.min()

    def delete_min(self):
        if self.root is not None:
            self.root = self.root.delete_min()
            if self.root is not None:
                self.root.color = BLACK

    def left_size(self):
        if self.root is None:
            return 0
        else:
            return self.root.left_size()

    def right_size(self):
        if self.root is None:
            return 0
        else:
            return self.root.right_size()

    def is_empty(self):
        return self.root is None

    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.size

    def is_red(self):
        return self.root is not None and self.root.is_red()

    def rotate_left(self):
        if self.root is None:
            return
        x = self.root.right
        self.root.right = x.left
        x.left = self.root
        x.color = x.left.color
        x.left.color = RED
        x.size = self.root.size
        self.root.size = 1 + self.root.left_size() + self.root.right_size()
        return x

    def rotate_right(self):
        if self.root is None:
            return
        x = self.root.left
        self.root.left = x.right
        x.right = self.root
        x.color = x.right.color
        x.right.color = RED
        x.size = self.root.size
        self.root.size = 1 + self.root.left_size() + self.root.right_size()
        return x

    def flip_colors(self):
        if self.root is None:
            return
        self.root.color = not self.root.color
        self.root.left.color = not self.root.left.color
        self.root.right.color = not self.root.right.color
