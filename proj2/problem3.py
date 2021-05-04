import sys
import heapq

class node():
    def __init__(self,freq, character) :
        self.left = None
        self.right = None
        self.character = character
        self.freq = freq
        self.direction = '' #0 - left, 1 - right

def find_leafnode(tree, char, code):
    newCode = str(code)
    newCode = newCode + str(tree.direction)
    if tree.left:
        find_leafnode(tree.left, char, newCode)
    if tree.right:
        find_leafnode(tree.right, char, newCode)
    if tree.character == char:
        print(char +" the code is - " + newCode)
        print("the tree direction is - " + str(tree.direction))
        return newCode
    

def printNodes(nodes):
    for node in nodes:
        print(node.character + " - " + str(node.freq))

# returns the data after it is encoded and the tree created from the initial data to encode the data
def huffman_encoding(data):
    char_count = dict()
    char_data = dict()  
    nodes = []
    for char in data:
        char_count[char] = data.count(char)
    for char in char_count:
        nodes.append(node(char_count[char], char))
    printNodes(nodes)
    print("******************")
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left = nodes[0]
        right = nodes[1]

        nodes.remove(left)
        nodes.remove(right)
        
        print("left removed: " + left.character)
        print("right removed: " + right.character)
        left.direction = 0
        right.direction = 1

        merge = node(left.freq+right.freq, left.character+right.character)
        merge.left = left
        merge.right = right

        nodes.append(merge)
        printNodes(nodes)
        print("******************")

    for char in char_count:
        char_code = find_leafnode(nodes[0], char, "")
        print(char_code)
        char_data[char] = char_code

    print(char_data)
    
    #huffman tree created now generated encoded data
    #for char in data:



        

    pass

# returns the decoded data(original data) using the hoffman tree
def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))