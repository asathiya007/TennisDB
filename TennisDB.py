from sys import argv
from os.path import exists

def writeNewFile(inptFile):
    plyrName = input("Enter the player's name: ")
    plyrAge = input("Enter the player's age: ")
    plyrHeight = input("Enter the player's height: ")
    plyrStyl = input("Enter the player's playing style: ")
    print()

    inptFile.write(f"Name: {plyrName}\n")
    inptFile.write(f"Age: {plyrAge}\n")
    inptFile.write(f"Height: {plyrHeight}\n")
    inptFile.write(f"Plays: {plyrStyl}\n")


script, file = argv

print("==============================")
print("||  TENNIS PLAYER DATABASE  ||")
print("==============================")
print()

if (exists(file)):
    print("The file exists, displaying data below.\n")
    plyrFile = open(file)
else:
    print("The file does not exist, please provide data below.")
    plyrFile = open(file, "w+")
    writeNewFile(plyrFile)

    print("Created file for player, displaying data below.\n")
    plyrFile.seek(0)

print(plyrFile.read())

plyrFile.close()
