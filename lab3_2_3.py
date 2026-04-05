class BinaryTree:
    def __init__(self, value):
        self.value = value
        self._left = None
        self._right = None

    def _dfs(self, is_right=False):
        if self._left is None and self._right is None and is_right:
            return self.value
        total = 0
        if self._left:
            total += self._left._dfs(False)
        if self._right:
            total += self._right._dfs(True)
        return total

    def branch_sums(self):
        return self._dfs(False)

    def build_tree(self, levels):
        values = [v for line in levels for v in line.split()]
        nodes = [None if v == "null" else BinaryTree(int(v)) for v in values]

        for i, node in enumerate(nodes):
            if node:
                li, ri = 2*i + 1, 2*i + 2
                if li < len(nodes):
                    node._left = nodes[li]
                if ri < len(nodes):
                    node._right = nodes[ri]
        return nodes[0]


with open("C:/Users/Qwerty_x/Desktop/labka/lab3(2)/binary_tree.txt", "r", encoding="utf-8") as f:
    tree = BinaryTree(0)              # створюємо тимчасовий об’єкт
    root = tree.build_tree(f.readlines())

print(root.branch_sums())       