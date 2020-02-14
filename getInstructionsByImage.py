from GetNumberByImage import getNumberByImage
from GetInstructionsByNumber import getInstructionByNumber

def getInstructionsByImage(file):
    number = getNumberByImage(file)
    instructions = getInstructionByNumber(number)
    return (instructions)

#test
myFile = 'barcode_img(test)/test4.jpg'
print(getInstructionsByImage(myFile))
