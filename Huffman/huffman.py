# Huffman Tree Encoder



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
                


class HuffmanTree():
    # only one none is needed, as that node refrences the rest of the tree
    def __init__(self, rootNode):
        self.rootNode = rootNode

    def printOut(self):
        self.rootNode.printOut()
    
    
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
            print(characterList)
            print(tree)
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

        
        if charA == None:        
            nodeA = newBranch
            nodeB = Node(valueB, charB, None, None)
        else:
            nodeA = Node(valueA, charA, None, None)
            nodeB = Node(valueB, charB, None, None)
            
        if charB == None:
            nodeA = Node(valueA, charA, None, None)
            nodeB = newBranch
        else:
            nodeA = Node(valueA, charA, None, None)
            nodeB = Node(valueB, charB, None, None)
            
            
        rootNode = Node(product, None, nodeA, nodeB)


        

        # recurse:

        return contsructTree(tempList, rootNode)
            



def main():
    charList = readText()# read text
    
    characterList = generateCharacterList(charList)# get list of character frequencies

    tree = contsructTree(characterList, None)

    huffman = HuffmanTree(tree) # generate tree

    for charac in characterList:
        charac.printOut()

    print("-------------------")
    
    huffman.printOut()

    # traverse tree

    # generate codes

    # encode text

main()
