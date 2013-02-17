# Huffman Tree Encoder


class Character():

    def __init__(self, char):
        self.char = char
        self.frequency = 0
        self.code = null

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def newInstance(self):
        self.frequency = self.frequency + 1

    def getFrequency(self):
        return self.frquency

class HuffmanTree():

    def __init__(self, chars):
        self.chars = chars # list of Character (class, not data type)
            
    
    
def readText():
    try:
        inFile = open("data.txt", "r")
        fileText = inFile.read()
        print(fileText)
    except (Exception):
        print("error: file not found")

def main():
    readText()# read text

    # generate tree

    # traverse tree

    # generate codes

    # encode text

main()
