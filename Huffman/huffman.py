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
        return self.frquency

    def printOut(self):
        print("-----Print Out-----")
        print("Char: " + self.char)
        print("Frequency: " + str(self.frequency))
        print("Code: " + self.code)
        

class HuffmanTree():

    def __init__(self, chars):
        self.chars = chars # list of Character (class, not data type)
            
    
    
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

    
          
    for charac in characterList:
        charac.printOut()

    return characterList
        




def main():
    charList = readText()# read text
    characterList = generateCharacterList(charList)
    

    # generate tree

    # traverse tree

    # generate codes

    # encode text

main()
