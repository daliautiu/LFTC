class TreeNode:
    def __init__(self, symbol):
        self.symbol = symbol    # identifier/constant
        self.left = None        # <
        self.right = None       # >


class SymbolTable:
    def __init__(self):
        self.root = None  # root of BST

    # insert a symbol in the tree
    def _insert(self, node, symbol):
        if node is None:
            return TreeNode(symbol)  # create a new node
        if symbol < node.symbol:
            node.left = self._insert(node.left, symbol)
        elif symbol > node.symbol:
            node.right = self._insert(node.right, symbol)
        return node

    # Public method
    def insert(self, symbol):
        self.root = self._insert(self.root, symbol)

    # search for a symbol
    def _search(self, node, symbol):
        if node is None:
            return False  # symbol not found
        if symbol == node.symbol:
            return True   # symbol found
        if symbol < node.symbol:
            return self._search(node.left, symbol)
        else:
            return self._search(node.right, symbol)

    # Public method
    def search(self, symbol):
        return self._search(self.root, symbol)

    # in-order traversal (alphabetical display)
    def _in_order(self, node):
        if node:
            self._in_order(node.left)         # left
            print(node.symbol, end=" ")       # node
            self._in_order(node.right)        # right

    # display the tree in alphabetical order
    def display(self):
        self._in_order(self.root)
        print()



if __name__ == "__main__":

    st = SymbolTable()

    st.insert("x")
    st.insert("y")
    st.insert("z")
    st.insert("a")
    st.insert("b")
    st.insert("42")
    st.insert("123")

    print("Symbol Table in alphabetical order:")
    st.display()

    search_key = "x"
    if st.search(search_key):
        print(f"{search_key} found in the symbol table.")
    else:
        print(f"{search_key} not found in the symbol table.")

    search_key = "abc"
    if st.search(search_key):
        print(f"{search_key} found in the symbol table.")
    else:
        print(f"{search_key} not found in the symbol table.")
