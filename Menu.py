"""
Author : Arunima Gulia
Last Modified : 1/31/21
Copyright : 2021, All Rights Reserved

Description: This class contains the method used to print the game menu
"""

class Titles:
   #This is the menu for the start of the game
    def intro(self):
        title = "Math Quiz"
        print(title)
        print("*" * len(title))
        operationMenu = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", "5. Exit"]
        print(operationMenu[0])
        print(operationMenu[1])
        print(operationMenu[2])
        print(operationMenu[3])
        print(operationMenu[4])
