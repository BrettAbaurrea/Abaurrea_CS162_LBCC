"""This is a program showing some of the basics of programming"""

#Variables
MyInt = 42
MyFloat = 3.14
Word = 'My "word" is actually multiple words'
#Value = 100
Char = 'a' #Not really a character data type

print(f"MyFloat: {MyFloat}")
print(f"Word: {Word}")
print(f"char[0]: {Char[0]}")

#Conditionals (Selections/If-Statements)
threshold = 4
if MyFloat > threshold:
    print(f"MyFloat ({MyFloat}) is greater than {threshold}")
elif MyFloat == threshold:
    print(f"MyFloat ({MyFloat}) is equal to {threshold}")
else:
    print(f"MyFloat ({MyFloat})is not greater than {threshold}")

#Repitition (Loops & Recursion)
for ForNumber in range(1,MyInt):
    print(f"Number: {ForNumber}") #Runs from 1-41

WhileNumber = 0
"""WhileNumber is a variable that should only be used within the values of 0-42""" #This is a docstring

while WhileNumber < MyInt: #Continue while this is true
    WhileNumber += 1    #1-42
    print (f"Number: {WhileNumber}")
    #WhileNumber += 1   #0-41

#Functions
def Dublin(input):
    """Dublin takes a numeric input, and returns double that input"""
    ScopedVariable = 9999
    print(f"ScopedVariable within Dublin Function: {ScopedVariable}")
    return input * 2

def SmartPrint(input):
    print (f"input:  {input}")
print (f"Dublin(MyInt): {Dublin(MyInt)}")
SmartPrint(MyInt)

print(Dublin) #Functions are Objects in Python

#input
#MyInput = input("Please enter a number from 1-100: ")
#print(f"MyInput: {MyInput}")

#Scope
#print(f"ScopedVariable: {ScopedVariable}") #Remove comment to recieve NameError!

#Classes
class Bottle:
    """A class that represents a bottle."""

    def __init__(self):
        self.material = "steel"

        self.volumeCap = 24
        self.volumeUnit = "ounces"

    def getMaterial(self):
        return self.material;

    def getVolume(self):
        """Construct a string representing the volume of the bottle with its unit."""
        return str(self.volumeCap) + " " + self.volumeUnit

    def setVolume(self, newVolumeCap, newVolumeUnit):
        """Set both the volumeCap and the volume unit."""
        self.volumeCap = newVolumeCap
        self.volumeUnit = newVolumeUnit

    def interactiveSetVolume(self):
        """Change a bottle's volume with user input."""
        newVolumeUnit = input("Please enter a unit of measure for our bottle: ")
        newVolumeCap = input("Please enter a capacity of that unit for our bottle: ")
        self.setVolume(newVolumeCap, newVolumeUnit)


#use my definitions to do something
myBottle = Bottle()

print(f"myBottle.material: {myBottle.material}")
print(f"myBottle.getVolume: {myBottle.getVolume()}")


myBottle.interactiveSetVolume()
print(f"myBottle.getVolume: {myBottle.getVolume()}")