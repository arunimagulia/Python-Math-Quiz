"""
Author : Arunima Gulia
Last Modified : 1/31/21
Copyright : 2021, All Rights Reserved

Description: Main class where the quiz is started and played
"""
import argparse
import TitleAndMainMenu
import QuestionsAndAnswers
import Utilities

#Main method used to run the game
def main():
    parser = argparse.ArgumentParser(description="Math Quiz")
    parser.add_argument('-o', '--output', action='store_true',
                        help="shows output and starts the game")
    args = parser.parse_args()
    if args.output:
        print("This is the start of the math quiz. Good Luck!")

    menu = TitleAndMainMenu.Titles()
    menu.intro()

    IO = Utilities.Operations()
    IO.separator()

    qans = QuestionsAndAnswers.Responses()

    option = IO.userInput()
    if option != 0:
        totalscore = 0
        correct = 0

        while totalscore != 10:
            totalscore = totalscore + 1
            correct = qans.askquestion(option, correct)

        IO.separator()
        IO.displayResults(totalscore, correct)
        print("Do you want to play again? Press 1 for yes or 0 to exit")
        IO.userinput = int(input("Enter your choice: "))
        if IO.userinput == 1:
            main()
        else:
            print("Exit the quiz.")

main()
