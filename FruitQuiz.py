import random

class FruitQuiz:
    def __init__(self):
        self.fruits={'Apple':'red',
                     'Orange':'orange',
                     'Watermelon':'green',
                     'Banana': 'yellow',
                     'Lemon':'yellow',
                     'Kiwi':'brown',
                     'Avocado':'green',
                     'Mango':'orange'}
   
    def quiz(self):
        while(True):

            fruits, color = random.choice(list(self.fruits.items()))
           

            print("What is the color of {}".format(fruits))
            user_answer = input()
            
            if(user_answer.lower() == color):
                print("Correct Answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0, if you want to play again, otherwise 1"))

            if (option):
                break

print("Welcome to Fruit Quiz")
fq = FruitQuiz()
fq.quiz()


            
                     
