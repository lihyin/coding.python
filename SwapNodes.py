#!/bin/python3

import os
import sys


#
# Complete the swapNodes function below.
#
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def listInOrder(self, node, l):
        if node is None:
            return

        self.listInOrder(node.left, l)
        l.append(node.value)
        self.listInOrder(node.right, l)

        return l

    def swap(self):
        temp = self.left
        self.left = self.right
        self.right = temp

    def find(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node

        r = self.find(node.left, value)
        if r is not None:
            return r

        r = self.find(node.right, value)
        if r is not None:
            return r

        return None


def swapNodes(indexes, queries):
    # Construct the tree
    root = Node(1, None, None)
    queue = [root]
    for e in indexes:
        node = queue[0]
        queue = queue[1:]

        if e[0] != -1:
            node.left = Node(e[0], None, None)
            queue.append(node.left)

        if e[1] != -1:
            node.right = Node(e[1], None, None)
            queue.append(node.right)

    result = []
    for q in queries:
        found = False
        node = root.find(root, q)
        if node is not None:
            node.swap()

        result.append(root.listInOrder(root, []))

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
