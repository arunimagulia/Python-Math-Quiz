"""
Author : Arunima Gulia
Last Modified : 1/31/21
Copyright : 2021, All Rights Reserved

Description: Class that contains the methods used to ask the quiz questions,
             capture the users answers, and check the answers.
"""
import random
class Responses:

    #Captures the users answer to the math problem
    def userAnswer(self, problem):
        try:
            for i in range(10):
                print("Enter your answer to the question")
                print(problem)
                result = int(input(" = "))
                return result
        except:
            print("Error: Invalid Input")
            pass

    #Used to check the user's answer to the question
    def checkAnswer(self, userSolution, solution, count):
        try:
            if userSolution == solution:
                count = count + 1
                print("Correct!")
                return count
            else:
                print("Incorrect :( ")
                return count
        except ValueError:
            return count

    #Used to ask the question after the user picks their choice of operation
    def askquestion(self,index, count):
        try:
            firstNumber = random.randrange(1, 21)
            secondNumber = random.randrange(1, 21)
            if index is 1:
                problem = str(firstNumber) + " + " + str(secondNumber)
                solution = firstNumber + secondNumber
                userSolution = self.userAnswer(problem)
                count = self.checkAnswer(userSolution, solution, count)
            elif index is 2:
                problem = str(firstNumber) + " - " + str(secondNumber)
                solution = firstNumber - secondNumber
                userSolution = self.userAnswer(problem)
                count = self.checkAnswer(userSolution, solution, count)
            elif index is 3:
                problem = str(firstNumber) + " * " + str(secondNumber)
                solution = firstNumber * secondNumber
                userSolution = self.userAnswer(problem)
                count = self.checkAnswer(userSolution, solution, count)
            elif index is 4:
                problem = str(firstNumber) + " // " + str(secondNumber)
                solution = firstNumber // secondNumber
                userSolution = self.userAnswer(problem)
                count = self.checkAnswer(userSolution, solution, count)
            else:
                return 0

            return count
        except ValueError:
            print("Error: Invalid Index")
            return 0
