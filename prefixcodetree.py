class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.leftNode = None
        self.rightNode = None

    def isLeafNode(self):
        return ((self.leftNode is None) and (self.rightNode is None))

class PrefixCodeTree:
    # Constructor
    def __init__(self):
        self.rootNode = Node('')

    def insert(self, codeword, symbol):
        node = self.rootNode

        for code in codeword:
            if (code == 0):
                if (node.leftNode is None):
                    node.leftNode = Node('')
                    node = node.leftNode
                else:
                    node = node.leftNode
            else:
                if (node.rightNode is None):
                    node.rightNode = Node('')
                    node = node.rightNode
                else:
                    node = node.rightNode

        node.symbol = symbol

    def decode(self, encodedData, datalen):
        result = ''

        decodeData = ''.join(["{:08b}".format(x) for x in encodedData])
        decodeData = ''.join(decodeData.split())
        decodeData = decodeData[:datalen]

        node = self.rootNode

        for i in range(datalen):
            if (decodeData[i] == '0'):
                node = node.leftNode
            else:
                node = node.rightNode

            if (node.isLeafNode()):
                result = result + node.symbol
                node = self.rootNode

        return result

if __name__ == "__main__":
    codebook = {
      'x1': [0],
      'x2': [1,0,0],
      'x3': [1,0,1],
      'x4': [1,1]
    }

    codeTree = PrefixCodeTree() # create a prefix code tree `codeTree`

    # Initialize codeTree with codebook
    for symbol in codebook:
        codeTree.insert(codebook[symbol], symbol)

    message = codeTree.decode(b'\xd2\x9f\x20', 21) 
    
    print(message)

