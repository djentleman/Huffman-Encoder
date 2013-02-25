# Huffman Tree Encoder

import time

class Character():

    def __init__(self, char):
        self.char = char
        self.frequency = 1 # to initlize there must be 1 of a char
        self.code = ""

    def getChar(self):
        return self.char

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def increment(self):
        self.frequency = self.frequency + 1

    def getFrequency(self):
        return self.frequency

    def printOut(self):
        print("-----Print Out-----")
        print("Char: " + self.char)
        print("Frequency: ", self.frequency)
        print("Code: " + self.code)
        
class Node():
    # represents a single node of a huffmanTree
    # frequency & char are Character attributes

    def __init__(self, value, char, leftNode, rightNode):
        # no char input (None) = product = not leaf
        self.value = value
        self.char = char
        self.leftNode = leftNode
        self.rightNode = rightNode

    def printOut(self):
        print("Node Value: ", self.value)
        if self.char == None:
            print("Node Char: ", None)
        else:
            print("Node Char: ", self.char)
        print("Children:")
        if self.leftNode == None:
            print("    Left Child (0):", None)
        else:
            print("    Left Child (0):", self.leftNode.printOut())
        if self.rightNode == None:
            print("    Right Child (1):", None)
        else:
            print("    Right Child (1):", self.rightNode.printOut())


    def inOrder(self):
        if self.leftNode != None:
            self.leftNode.inOrder()
        print("-------------------")
        print("Value: ", self.value)
        print("Char: ", self.char)
        print("-------------------")
        if self.rightNode != None:
            self.rightNode.inOrder()

    def preOrder(self):
        print("-------------------")
        print("Value: ", self.value)
        print("Char: ", self.char)
        print("-------------------")
        if self.leftNode != None:
            self.leftNode.preOrder()
        if self.rightNode != None:
            self.rightNode.preOrder()

    def postOrder(self):
        if self.leftNode != None:
            self.leftNode.postOrder()
        if self.rightNode != None:
            self.rightNode.postOrder()
        print("-------------------")
        print("Value: ", self.value)
        print("Char: ", self.char)
        print("-------------------")

    def huffmanSearch(self, search, code):
        
        if self.char == search:
            #print(self.char + " = " + code)
            
            # save to temp file

            outFile = open("temp.txt", "w")
            outFile.write(code)
            outFile.close()


            #return code
        
        
        if self.leftNode != None:
            code = code + "1"
            codeToReturn = self.leftNode.huffmanSearch(search, code)
            # pop codeToReturn out
            
        code = removeLastChar(code) # 'goes back up a node'
        
        if self.rightNode != None:
            code = code + "0"
            codeToReturn = self.rightNode.huffmanSearch(search, code)
            # pop codeToReturn out


        


class HuffmanTree():
    # only one node is needed, as that node refrences the rest of the tree
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def printOut(self):
        self.rootNode.printOut()

    def inOrder(self):
        print("In Order Traversal")
        self.rootNode.inOrder()

    def preOrder(self):
        print("Pre Order Traversal")
        self.rootNode.preOrder()

    def postOrder(self):
        print("Pre Order Traversal")
        self.rootNode.postOrder()

    def huffmanSearch(self, search):
        self.rootNode.huffmanSearch(search, "")

def removeLastChar(string):
    newStr = ""
    for i in range(len(string)):
        if i != (len(string) - 1):
            newStr = newStr + string[i]
    return newStr
            
        
    
    
def readText():
    try:
        inFile = open("data.txt", "r")
        fileText = inFile.read()

        # next step: get from string to list of characters

        charList = []

        for ch in fileText:
            charList.append(ch)

        #charList is a list of all chars

        return charList

        inFile.close()
                    
    except (Exception):
        print("error: file not found")

        return null

def generateCharacterList(charList):
    characterList = [] # list of Characters
    
    for char in charList: # cycle through characters in text files
        
        if len(characterList) != 0: # for nonempty Characterlists
            isContained = False
            
            for charac in characterList: # cycle through CharacterList
                if char == charac.getChar(): # if char from txt alreadt exists
                    charac.increment() # incrememnt frequency
                    isContained = True
                    
            if isContained == False: # if char is 'new'
                characterList.append(Character(char)) # create Character
                
        else:
            characterList.append(Character(char)) # if empty list, add to it

    
          
    #for charac in characterList:
        #charac.printOut()

    return characterList
        
def getLowestVal(tempList):
    charToRemove = None

    lowestVal = 99999
    
    for charac in tempList: # get tupleValA


        
        if type(charac) == Character:
            if charac.getFrequency() < lowestVal:
                lowestVal = charac.getFrequency()
                charToRemove = charac
                
        elif type(charac) == int:
            if charac < lowestVal:
                lowestVal = charac
                charToRemove = charac

    return charToRemove

def removeCharac(charToRemove, tempList):
    newList = []
    for charac in tempList:
        if charac != charToRemove:
            newList.append(charac)

    return newList

def contsructTree(characterList, tree):

    if len(characterList) == 1:
        if tree != None:
            ##print(characterList)
            ##print(tree)
            return tree
    else:
    
        tempList = characterList # tempList will get depleted
        # get two lowest frequencies
        lowItemA = None
        lowItemB = None 

        # get tupleValA

        charToRemove = getLowestVal(tempList)

        lowItemA = charToRemove

        #remove charToRemove
        
        tempList = removeCharac(charToRemove, tempList)


        # get tupleValB

        charToRemove = getLowestVal(tempList)

        lowItemB = charToRemove

        # remove charToRemove

        tempList = removeCharac(charToRemove, tempList)
        

        # extract values

        if type(lowItemA) == Character:
            valueA = lowItemA.frequency
            charA = lowItemA.char
        else:
            valueA = lowItemA
            charA = None

        if type(lowItemB) == Character:
            valueB = lowItemB.frequency
            charB = lowItemB.char
        else:
            valueB = lowItemB
            charB = None

        # get product

        product = valueA + valueB
        

        #print (valueA, charA)
        #print (valueB, charB)
        #print ("product: ", product)

        tempList.append(product) # add product to tempList

        newBranch = tree # current root node will now be a branch

        if tree == None:
            
            nodeA = Node(valueA, charA, None, None)
            nodeB = Node(valueB, charB, None, None)
                
            rootNode = Node(product, None, nodeA, nodeB)
            
        else:
            if charA == None:        
                nodeA = newBranch
                nodeB = Node(valueB, charB, None, None)
                rootNode = Node(product, None, nodeA, nodeB)
            elif charB == None:
                nodeA = Node(valueA, charA, None, None)
                nodeB = newBranch
                rootNode = Node(product, None, nodeA, nodeB)
            else:
                nodeA = Node(valueA, charA, None, None)
                nodeB = Node(valueB, charB, None, None)
                newBranch2 = Node(product, None, nodeA, nodeB)

                newProduct = product + newBranch.value
                tempList.append(newProduct)
                tempList = removeCharac(product, tempList)

                rootNode = Node(newProduct, None, newBranch, newBranch2)
                
            
            



        

        # recurse:

        return contsructTree(tempList, rootNode)
            


def saveEncodedFile(encodedStr):
    outFile = open("encodedString.txt", "w")
    outFile.write(encodedStr)
    outFile.close()


def finalPrintout():
    originalFile = open("data.txt", "r")
    text = originalFile.read()
    originalSize = len(text) * 256
    print("Original Text: " + text)
    print("Size: " + str(len(text) * 256) + " Bytes")

    originalFile.close()

    encodedFile = open("encodedString.txt", "r")
    huffmanText = encodedFile.read()
    compressionSize = len(huffmanText)
    print("Compressed Text: " + huffmanText)
    print("Size: " + str(len(huffmanText)) + " Bytes")
    encodedFile.close()

    compressionRatio = originalSize / compressionSize
    compressionRatio = int(compressionRatio)

    print("Compression Ratio: " + str(compressionRatio) + ":1")

def main():
    start = time.clock()
    
    charList = readText()# read text
    
    characterList = generateCharacterList(charList)# get list of character frequencies

    tree = contsructTree(characterList, None) # generate tree

    huffman = HuffmanTree(tree)

    # ---------------------------------------------------

    for charac in characterList: # traverse tree
        huffman.huffmanSearch(charac.char) # generate codes


        inFile = open("temp.txt", "r")
        code = inFile.read()

        charac.code = code
        #charac.printOut() # debug

        inFile.close()

    # --------------------------------------------------
    

    encodedStr = ""

    for ch in charList: # loop through string
        for charac in characterList: # loop through characters
            # lol terrible time effic
            if ch == charac.char:
                encodedStr += str(charac.code)     # encode text
                
    #print(encodedStr)

    # -------------------------------------------------

    saveEncodedFile(encodedStr) # saves encoded string to file

    finalPrintout() # displays original string & huffman code on console

    elapsed = (time.clock() - start)
    print("Computation Time: " + str(elapsed) + "ms")

        


main()
