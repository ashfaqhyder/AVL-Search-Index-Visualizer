from time import perf_counter

from flask import Flask, jsonify, render_template, request


app = Flask(__name__)


class AVLNode:
    """Node used by the AVL tree."""

    def __init__(self, keyword):
        self.keyword = keyword
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """Self-balancing Binary Search Tree implementation."""

    def __init__(self):
        self.root = None
        self.last_rotation = "None"

    def height(self, node):
        return node.height if node else 0

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, keyword):
        self.last_rotation = "None"
        inserted, self.root = self._insert(self.root, keyword)
        return inserted

    def _insert(self, node, keyword):
        if node is None:
            return True, AVLNode(keyword)

        if keyword < node.keyword:
            inserted, node.left = self._insert(node.left, keyword)
        elif keyword > node.keyword:
            inserted, node.right = self._insert(node.right, keyword)
        else:
            return False, node

        self.update_height(node)
        return inserted, self._rebalance_after_insert(node, keyword)

    def _rebalance_after_insert(self, node, keyword):
        balance = self.balance_factor(node)

        if balance > 1 and keyword < node.left.keyword:
            self.last_rotation = "LL Rotation (Right Rotate)"
            return self.rotate_right(node)

        if balance < -1 and keyword > node.right.keyword:
            self.last_rotation = "RR Rotation (Left Rotate)"
            return self.rotate_left(node)

        if balance > 1 and keyword > node.left.keyword:
            self.last_rotation = "LR Rotation (Left then Right)"
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and keyword < node.right.keyword:
            self.last_rotation = "RL Rotation (Right then Left)"
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def delete(self, keyword):
        self.last_rotation = "None"
        deleted, self.root = self._delete(self.root, keyword)
        return deleted

    def _delete(self, node, keyword):
        if node is None:
            return False, node

        if keyword < node.keyword:
            deleted, node.left = self._delete(node.left, keyword)
        elif keyword > node.keyword:
            deleted, node.right = self._delete(node.right, keyword)
        else:
            deleted = True
            if node.left is None:
                return True, node.right
            if node.right is None:
                return True, node.left

            successor = self._min_value_node(node.right)
            node.keyword = successor.keyword
            _, node.right = self._delete(node.right, successor.keyword)

        if node is None:
            return deleted, node

        self.update_height(node)
        return deleted, self._rebalance_after_delete(node)

    def _rebalance_after_delete(self, node):
        balance = self.balance_factor(node)

        if balance > 1 and self.balance_factor(node.left) >= 0:
            self.last_rotation = "LL Rotation after delete"
            return self.rotate_right(node)

        if balance > 1 and self.balance_factor(node.left) < 0:
            self.last_rotation = "LR Rotation after delete"
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.balance_factor(node.right) <= 0:
            self.last_rotation = "RR Rotation after delete"
            return self.rotate_left(node)

        if balance < -1 and self.balance_factor(node.right) > 0:
            self.last_rotation = "RL Rotation after delete"
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, keyword):
        steps = 0
        current = self.root

        while current:
            steps += 1
            if keyword == current.keyword:
                return True, steps
            if keyword < current.keyword:
                current = current.left
            else:
                current = current.right

        return False, steps

    def to_dict(self):
        return self._node_to_dict(self.root)

    def _node_to_dict(self, node):
        if node is None:
            return None

        return {
            "keyword": node.keyword,
            "height": node.height,
            "balance": self.balance_factor(node),
            "left": self._node_to_dict(node.left),
            "right": self._node_to_dict(node.right),
        }


class BSTNode:
    """Node used by the normal unbalanced BST."""

    def __init__(self, keyword):
        self.keyword = keyword
        self.left = None
        self.right = None


class BST:
    """Classic Binary Search Tree without self-balancing."""

    def __init__(self):
        self.root = None

    def insert(self, keyword):
        if self.root is None:
            self.root = BSTNode(keyword)
            return True

        current = self.root
        while True:
            if keyword < current.keyword:
                if current.left is None:
                    current.left = BSTNode(keyword)
                    return True
                current = current.left
            elif keyword > current.keyword:
                if current.right is None:
                    current.right = BSTNode(keyword)
                    return True
                current = current.right
            else:
                return False

    def delete(self, keyword):
        deleted, self.root = self._delete(self.root, keyword)
        return deleted

    def _delete(self, node, keyword):
        if node is None:
            return False, None

        if keyword < node.keyword:
            deleted, node.left = self._delete(node.left, keyword)
            return deleted, node

        if keyword > node.keyword:
            deleted, node.right = self._delete(node.right, keyword)
            return deleted, node

        if node.left is None:
            return True, node.right
        if node.right is None:
            return True, node.left

        successor = self._min_value_node(node.right)
        node.keyword = successor.keyword
        _, node.right = self._delete(node.right, successor.keyword)
        return True, node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, keyword):
        steps = 0
        current = self.root

        while current:
            steps += 1
            if keyword == current.keyword:
                return True, steps
            if keyword < current.keyword:
                current = current.left
            else:
                current = current.right

        return False, steps

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def to_dict(self):
        return self._node_to_dict(self.root)

    def _node_to_dict(self, node):
        if node is None:
            return None

        return {
            "keyword": node.keyword,
            "height": self._height(node),
            "balance": None,
            "left": self._node_to_dict(node.left),
            "right": self._node_to_dict(node.right),
        }


avl_tree = AVLTree()
bst_tree = BST()
last_search = {"keyword": None, "avl_steps": 0, "bst_steps": 0, "found": False}


def clean_keyword(value):
    """Normalize user input so comparisons remain predictable."""
    return (value or "").strip().lower()


def response_payload(message, status="success"):
    return jsonify(
        {
            "status": status,
            "message": message,
            "tree": get_tree_payload(),
        }
    )


def get_tree_payload():
    avl_height = avl_tree.height(avl_tree.root)
    bst_height = bst_tree.height()
    return {
        "avl": avl_tree.to_dict(),
        "bst": bst_tree.to_dict(),
        "metrics": {
            "avl_height": avl_height,
            "bst_height": bst_height,
            "height_difference": bst_height - avl_height,
            "rotation": avl_tree.last_rotation,
            "last_search": last_search,
            "avl_complexity": "O(log n)",
            "bst_complexity": "O(n) worst case",
        },
    }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/insert", methods=["POST"])
def insert_keyword():
    keyword = clean_keyword(request.json.get("keyword"))
    if not keyword:
        return response_payload("Please enter a keyword.", "error")

    avl_inserted = avl_tree.insert(keyword)
    bst_tree.insert(keyword)

    if not avl_inserted:
        return response_payload(f"'{keyword}' already exists in the index.", "warning")

    return response_payload(f"Inserted '{keyword}' into AVL and BST indexes.")


@app.route("/delete", methods=["POST"])
def delete_keyword():
    keyword = clean_keyword(request.json.get("keyword"))
    if not keyword:
        return response_payload("Please enter a keyword.", "error")

    deleted = avl_tree.delete(keyword)
    bst_tree.delete(keyword)

    if not deleted:
        return response_payload(f"'{keyword}' was not found.", "warning")

    return response_payload(f"Deleted '{keyword}' from both indexes.")


@app.route("/search", methods=["POST"])
def search_keyword():
    keyword = clean_keyword(request.json.get("keyword"))
    if not keyword:
        return response_payload("Please enter a keyword.", "error")

    start = perf_counter()
    avl_found, avl_steps = avl_tree.search(keyword)
    avl_time = (perf_counter() - start) * 1000

    start = perf_counter()
    bst_found, bst_steps = bst_tree.search(keyword)
    bst_time = (perf_counter() - start) * 1000

    last_search.update(
        {
            "keyword": keyword,
            "avl_steps": avl_steps,
            "bst_steps": bst_steps,
            "found": avl_found and bst_found,
            "avl_time_ms": round(avl_time, 5),
            "bst_time_ms": round(bst_time, 5),
        }
    )

    if avl_found:
        return response_payload(
            f"Found '{keyword}'. AVL took {avl_steps} step(s); BST took {bst_steps} step(s)."
        )

    return response_payload(
        f"'{keyword}' was not found. AVL checked {avl_steps} node(s); BST checked {bst_steps} node(s).",
        "warning",
    )


@app.route("/get_tree_data")
def get_tree_data():
    return jsonify(get_tree_payload())


@app.route("/reset", methods=["POST"])
def reset_tree():
    global avl_tree, bst_tree, last_search
    avl_tree = AVLTree()
    bst_tree = BST()
    last_search = {"keyword": None, "avl_steps": 0, "bst_steps": 0, "found": False}
    return response_payload("Index reset successfully.")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
