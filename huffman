import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def encode(node, prefix, code):
    if node is None:
        return
    if node.char is not None:
        code[node.char] = prefix
    encode(node.left, prefix + '0', code)
    encode(node.right, prefix + '1', code)


def huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    return heap[0]


def calculate_tree_size(frequencies, letters):
    tree = huffman_tree(frequencies)
    code = defaultdict(str)
    encode(tree, '', code)
    tree_size = sum([len(code[char]) * freq for char, freq in frequencies.items() if char in letters])
    return tree_size

# character frequencies
frequencies = {
    'a': 200,
    'b': 250,
    'c': 100,
    'd': 350,
    'e': 400
}
#Write the letters you want to calculate the size for
letters = ['a','b','c','d','e']
print("Huffman tree size for letters {} : ".format(letters), calculate_tree_size(frequencies, letters))
