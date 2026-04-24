class Node:
    def __init__(self, key, value, left=None, right=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if self.root is None:
            self.root = Node(key, val)
        else:
            self._insert_helper(self.root, key, val)

    def _insert_helper(self, node, key, value):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_helper(node.left, key, value)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_helper(node.right, key, value)
        else:
            node.value = value

    def get(self, key: int) -> int:
        return self._get_helper(self.root, key)

    def _get_helper(self, node, key):
        if node is None:
            return -1
        if key < node.key:
            return self._get_helper(node.left, key)
        elif key > node.key:
            return self._get_helper(node.right, key)
        else:
            return node.value

    def getMin(self) -> int:
        if self.root is None:
            return -1
        node = self._find_min_node(self.root)
        return node.value

    def _find_min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    def getMax(self) -> int:
        if self.root is None:
            return -1
        node = self._find_max_node(self.root)
        return node.value

    def _find_max_node(self, node):
        while node.right is not None:
            node = node.right
        return node

    def remove(self, key: int) -> None:
        self.root = self._remove_helper(self.root, key)

    def _remove_helper(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._remove_helper(node.left, key)
        elif key > node.key:
            node.right = self._remove_helper(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            min_node = self._find_min_node(node.right)
            node.key = min_node.key
            node.value = min_node.value
            node.right = self._remove_helper(node.right, min_node.key)
        return node

    def getInorderKeys(self) -> List[int]:
        return self._traversal_helper(self.root)

    def _traversal_helper(self, node):
        if node is None:
            return []
        return self._traversal_helper(node.left) + [node.key] + self._traversal_helper(node.right)
