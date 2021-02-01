"""
Author : Arunima Gulia
Last Modified : 1/31/21
Copyright : 2021, All Rights Reserved

Description: Class used to get the operation of choice from the user, and display quiz results
"""
class Operations():

    #Used to get the choosen operation from the user
    def userInput(self):
        try:
            userChoice = int(input("Enter your operation of choice: "))
            if isinstance(userChoice, int):
                print(userChoice)
                if int(userChoice):
                    while userChoice > 5 or userChoice <= 0:
                        print("Invalid menu option.")
                        userChoice = int(input("Please enter a valid option: "))
                    else:
                        return userChoice
            else:
                print("enter a number between 1 and 5")
                return 0
        except:
            print("Invalid Input: enter a number between 1 and 5")

    #Prints the quiz results
    def displayResults(self, total, correct):
        if total > 0:
            result = correct / total

        print("You answered", correct, "questions correctly out of", total, "questions.")

    def separator(self):
        print("-" * 24)
