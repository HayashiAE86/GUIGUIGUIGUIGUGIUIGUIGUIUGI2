from tkinter import *
import random

names = [] 
global questions_answers
asked = []
score = 0
questions_answers = {
  1: ["What is this car brand?", 'Fiat', 'Peugeot', 'Citroen', 'Abarth',10],
  2: ["What is this car brand?", 'Honda' ,'Hyundai',3],
  3: ["Where this car brand is from?", 'Italy', 'Japan', 'America', 'UK',3],
  4: ["What is the common point about this car brands?", 'Both are from italy', 'Both brand have bad cars', 'Both brand have more than 20 years of history',5],
  5: ["What is relation ships between Toyota and Lexus?",'Both brand are same but logo is different', 'Both brands are same but one of them is for over sea',5],
  6: ["Where this car brand is from?", 'Germany', 'Japan', 'Korea', 'UK', 'France',3],
  7: ["What is relation ship between this car brands?", 'Both brands were rival back than', 'Both car is very hard to maintain.',10],
  8: ["Why this car from this brand is really expensive?", 'Because they made fastest car in the world.', 'They use expensive components to build each car.',10],
}

def randomiser():
  global qnum
  qnum = random.randint(1,10)

if qnum not in asked:
   asked.append(qnum)
elif qnum in asked:
   randomiser()

randomiser()

class Quiz:
 def __init__(self, parent):
   background_color="OldLace"

  
   self.heading_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
   self.user_label.grid(row=0, padx=20)