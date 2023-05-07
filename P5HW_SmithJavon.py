# Randomized math quiz
# 5/4/2023
# CTI-110 P5HW - Math Quiz
# Javon Smith
#

# -*- coding: utf-8 -*-
    
import random

'''
generates random number and returns
'''
def generateRandomNo():
    return random.randint(10, 999)
    
'''
checks whether the guess made is correct or not
'''
def checkGuess(number, guess):
    if (guess < number):
        print("Sorry, guess is too low.")
        return 0
    if (guess > number):
        print("Sorry, guess is too high.")
        return 0
    if (guess == number):
        print("Congratulations!!!! your answer is correct..")
        return 1
        
    #Constructor
    def __init__(self):
        self.head = None
    #Method to add a student to the linked list
    def add_student(self, s:Student):
        if self.head is None:
            self.head = s
        else:
            temp = self.head
            while temp.getNext() != None :
                temp = temp.getNext()
            temp.setNext(s)
                

    #Method to pay tution fee to the student at index 'i' in the linked list
    def pay_tution (self, i, amt):
        k = 0
        temp = self.head
        while temp != None:
            if k == i:
                temp.setStudentBalance (temp.getStudentBalance() - amt)
                temp = temp.getNext()
                k + 1
                
    #Method to display list of students in the linked list
    def show(self):
        temp = self.head
        if temp!= None:
            print("{0:<6}{1:<8}{2}".format("ID", "Name", "Balance"))
            while temp != None:
                print("{0:<6}{1:<8}{2:.2E}".format(str(temp.getStudentID()).zfill(2), temp.getStudentName(), temp.getStudentBalance()))
                temp = temp.getNext()
    #Method to clear the students whose balance is 0
    def clear(self):
        temp = self.head
        newList = None
        while temp != None:
            if temp.getStudentBalance() != 0:
                if newList is None:
                    newList = Student (temp.getStudentId(), temp.getStudentName(), temp.getStudentBalance(), None)
                else:
                    temp2 = newList
                    while temp2.getNext() != None:
                        temp2 = temp2.getNext()
                        self. head = newList
def main():
    print("\nWelcome to Math Quiz")
    #Loops as long as user wants to continue
    while True:
        choice = menu()
        if choice == 1:
            a = generateRandomNo()
            b = generateRandomNo()
            print("  "+ str(a) + "\n+ " + str(b))
            ans = a + b
            guess = int(input("Enter answer.\n"))
            i = 1
            while(checkGuess(ans, guess) != 1 ):
                guess = int(input("try again: "))  
                i = i + 1
            print("Number of guesses: "+str(i))
        elif choice == 2:
            a = generateRandomNo()
            b = generateRandomNo()
            print("  "+ str(a) + "\n- " + str(b))
            ans = a - b
            guess = int(input("Enter answer.\n"))
            i = 1
            while(checkGuess(ans, guess) != 1 ):
                guess = int(input("try again: "))  
                i = i + 1
            print("Number of guesses: "+str(i))
        elif choice == 3:
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid option... Try again")
            
        
'''
Method to display menu and read choice from user 
'''   
def menu():
    print("\nMAIN MENU")
    print("-----------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
    choice = int(input("Please choose one of the menu options: "))
    return choice

main()
