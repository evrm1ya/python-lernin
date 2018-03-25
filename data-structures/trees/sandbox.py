import json
from Node import Node
from BST import BST

def simple_traversal():
    n1 = Node('root')
    n2 = Node('left child')
    n3 = Node('right child')
    n4 = Node('left grandchild')

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4

    current = n1

    while current:
        print(current.data)
        current = current.left_child

def print_json(obj):
    print(json.dumps(obj, indent=2))

def bst_1():
    bst = BST()
    bst.insert(3)
    bst.insert(6)

    print(bst)

    #print_json(bst)

if __name__ == '__main__':
    simple_traversal()

    bst_1()
