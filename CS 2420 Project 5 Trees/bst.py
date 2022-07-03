class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def is_empty(root):
    if root.data is None and root.left is None and root.right is None:
        return True
    return False


def size(root):
    if root.data is None:
        return 0
    return len(inorder(root))


def height(root):
    if root is None or root.data is None:
        return 0
    tall = 1
    if root.left is not None or root.right is not None:
        tall += max((height(root.left), height(root.right)))
    return tall


def add(root, item):
    if root is None:
        return BST(item)
    if root.data is None:
        root.data = item
    elif root.data.letter == item.letter:
        root.data.count += 1
    elif item.letter < root.data.letter:
        root.left = add(root.left, item)
    elif item.letter > root.data.letter:
        root.right = add(root.right, item)
    return root


def remove(root, item):
    if root is None:
        return root

    if item.letter < root.data.letter:
        root.left = remove(root.left, item)
    elif item.letter > root.data.letter:
        root.right = remove(root.right, item)

    elif item.letter == root.data.letter:
        # If 0 or 1 child nodes, rede said nodes accordingly
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
            root.data = root.right
            return root.data
        elif root.right is None:
            root.data = root.left
            return root.data
        else:
            # If 2 child nodes, redo nodes accordingly
            temp_root = root.right
            while temp_root.left is not None:
                temp_root = temp_root.left
            remove(root, temp_root.data)
            root.data = temp_root.data
    return root


def find(root, item):
    if is_empty(root):
        raise ValueError
    lyst = inorder(root)
    for i in lyst:
        if i.letter == item.letter:
            return i
    raise ValueError


def inorder(root):
    my_list = []
    if root:
        my_list += inorder(root.left)
        my_list.append(root.data)
        my_list += inorder(root.right)
    return my_list


def preorder(root):
    my_list = []
    if root:
        my_list.append(root.data)
        my_list += preorder(root.left)
        my_list += preorder(root.right)
    return my_list


def postorder(root):
    my_list = []
    if root:
        my_list += postorder(root.left)
        my_list += postorder(root.right)
        my_list.append(root.data)
    return my_list


def rebalance(root):
    my_list = inorder(root)
    root = find_center(my_list)
    return root


def find_center(lyst):
    center = lyst.index(lyst[len(lyst) // 2])
    root = BST(lyst[center])
    try:
        root.left = find_center(lyst[:center])
        root.right = find_center(lyst[center + 1:])
    except IndexError:
        pass
    return root
