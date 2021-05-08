""" 
the encoding and decoding sections were assisted by mentor: Mahmoud R

 """
import sys

class node():
    def __init__(self,freq, character) :
        self.left = None
        self.right = None
        self.character = character
        self.freq = freq
        self.direction = '' #0 - left, 1 - right
    
def printNodes(nodes):
    for node in nodes:
        print(node.character + " - " + str(node.freq))

# returns the data after it is encoded and the tree created from the initial data to encode the data
class Huffman_Coding:
    def find_leafnodes(tree, current_code):
        codes = dict()
        if tree == None:
            return codes
        if tree.character is not None:
            codes[tree.character] = current_code

        codes.update(Huffman_Coding.find_leafnodes(tree.left, current_code + "0"))
        codes.update(Huffman_Coding.find_leafnodes(tree.right, current_code + "1"))
        return codes

    def huffman_encoding(data):
    
        char_count = dict()  
        nodes = []
        for char in data:
            char_count[char] = data.count(char)
        for char in char_count:
            nodes.append(node(char_count[char], char))
        if len(nodes) < 1:
            return None, None

        if len(nodes) == 1:
            left, right = nodes[0], nodes[0]
            merge = node(left.freq+right.freq, left.character+right.character)
            merge.left = left
            nodes.remove(left)
            nodes.append(merge)
    
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes[0]
            right = nodes[1]

            nodes.remove(left)
            nodes.remove(right)
            left.direction = 0
            right.direction = 1

            merge = node(left.freq+right.freq, left.character+right.character)
            merge.left = left
            merge.right = right

            nodes.append(merge)

        char_data = Huffman_Coding.find_leafnodes(nodes[0],"")
        
        #huffman tree created now generated encoded data
        encoded_text = Huffman_Coding.get_huffman_encoded_text(data, char_data)
        return encoded_text, nodes[0]
        pass

    def get_huffman_encoded_text(text, codes):
        encoded_text = "" 
        for char in text:
            encoded_text += codes[char]
        return encoded_text

    # returns the decoded data(original data) using the hoffman tree
    def huffman_decoding(encoded_text,tree):
        decoded_text = ""
        if encoded_text == "" or encoded_text == None:
            return decoded_text
        current_node = tree
        for char in encoded_text:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.left == None and current_node.right == None:
                decoded_text += current_node.character
                current_node = tree
        return decoded_text

        pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print("Test Case 1")
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Coding.huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Coding.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "BBBBBBB"

    print("Test Case 2")
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Coding.huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Coding.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = ""

    print("Test case 3")
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = Huffman_Coding.huffman_encoding(a_great_sentence)

    #print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = Huffman_Coding.huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))