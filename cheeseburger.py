"""
This program decides whether the user should eat a cheese burgur
"""

#this part of the program takes input from the user
print("are you hungry? (y or n)")
hungry = input()
if hungry == 'y':
    print("do you like cheeseburgurs? (y or n)")
    like = input()
    
    print("are you allergic to cheeseburgurs? (y or n)")
    allergic = input()

#This part of the program decides of the user should eat a cheeseburgur
if hungry == 'y' and like == 'y' and allergic == 'n':
    print("you should eat a cheeseburger")
else:
    print("you should not eat a cheeseburger")
