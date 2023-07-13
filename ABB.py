from ler_xls import read_xls_file

class Node:
    def __init__(self, key, value):
        self.key = str(key)
        self.value = str(value)
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_recursive(self.root, key, value)

    def _insert_recursive(self, node, key, value):
        if str(key) < node.key:
            if node.left is None:
                node.left = Node(key, value)
            else:
                self._insert_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node(key, value)
            else:
                self._insert_recursive(node.right, key, value)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


# Example usage
matrix = read_xls_file()
bst = BinarySearchTree()

for row in matrix:
    key = row[0]
    value = row[1]
    bst.insert(key, value)

# Example usage
search_key = input("Digite a chave de busca:")
result = bst.search(search_key)

if result is not None:
    print(f"Value for key {search_key}: {result.value}")
else:
    print(f"No value found for key {search_key}")


