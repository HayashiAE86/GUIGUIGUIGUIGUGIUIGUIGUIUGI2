from tkinter import *

from PIL import Image, ImageTk

import random
names = []
global questions_answers
asked = []
score = 0
questions_answers = {
    1: [
        "Which car brand is from England?",
        "Volvo",
        "Lotus",
        "Buick",
       
    4],
    2: [
        "What is the official name of the Lamborghini?:",
        'Lamborghini Auto. SA', 'Automobili S.p.A.Lamborghini ',
        'Automobili Italia Lamborghini', 4
    ],
    3: [
        "What is common problem cause in europian cars?",
        'Gas tank is very weak', 'Electrical gremlins', 'They have no GPS', 4
    ],
    4: [
        "Which one is italian car brand?", 'Alfa Romeo', 'BSA', 'Liberty Walk',
        2
    ],
    5: [
        "Why is JDM(Japanese Domestic Market) cars are famous?",
        'Because they are fuel efficient and produce less CO2 so that we can make less polution to air.',
        'Because they are cheap.',
        'people are obsessed with JDM cars how tuneable they are and how easy they are to personalize.',
        'Because they are trend in Instagram, TikTok or anyother SNSs.', 7
    ],
    6: [
        "Which car brand is rare super car brand from Japan?", 'Mitsuoka',
        'Tomy Kaira', 'Dome', 4
    ],
    7: [
        "Which car brand is from Germany?", 'Triumph', 'Maserati', 'SAAB',
        'Opel', 4
    ],
    8: [
        "Which car is most expensive car in the world?",
        '2006 Yes! Roadstar 3.2', '2017 Devel sixteen Prototype',
        '1955 Mercedes-Benz SLR Uhlenhaut Coupe', 4
    ],
    9: ["When car brand Honda started?", '1959', '1948', '1910', 4],
    10: [
        "To avoid being blinded by headlights of another vehicle coming towards you what should you do?",
        "Look to the left of the road", "Look to the centre of the road",
        "Wear sunglasses that have sufficient strength",
        "Look to the right side of the road", "Look to the left of the road", 1
    ],
}


def randomiser():
    global qnum
    qnum = random.randint(1, 10)

    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()


randomiser()


class QuizStarter:
    def __init__(self, parent):
        background_color = "OldLace"
      
        self.bg_image = Image.open("Car brand logo (1).png")
        self.bg_image = self.bg_image.resize((800, 400), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image) 
      
        self.quiz_frame=Frame(parent, bg = background_color,padx=100,
                                pady=100)
        self.quiz_frame.grid()         
       
        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1) 
        

        self.heading_label = Label(self.quiz_frame,
                                   text="CAR BRAND QUIZ",
                                   font=("Arial", "18", "bold"),
                                   bg=background_color)
        self.heading_label.grid(row=0, padx=20)

        self.user_label = Label(
            self.quiz_frame,
            text="Enter your username below and click start! ",
            font=("Arial", "18"),
            bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=2, padx=20, pady=20)

        self.continue_button = Button(self.quiz_frame,
                                      text="Start",
                                      font=("Helvetica", "13", "bold"),
                                      bg="orange",
                                      command=self.name_collection)
        self.continue_button.grid(row=3, padx=20, pady=20)

    def name_collection(self):
        name = self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


randomiser()


class Quiz:
    def __init__(self, parent):
        background_color = "OldLace"
        self.quiz_frame = Frame(parent, bg=background_color, padx=40, pady=40)
        self.quiz_frame.grid()
        self.question_label = Label(self.quiz_frame,
                                    text=questions_answers[qnum][0],
                                    font=("Tw Cen Mt", "16"),
                                    bg=background_color)
        self.question_label.grid(row=1, padx=10, pady=10)
        self.var1 = IntVar()
        self.rb1 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][1],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=1,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="White")
        self.rb1.grid(row=2, sticky=W)
        self.rb2 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][2],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=2,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="White")
        self.rb2.grid(row=3, sticky=W)
        self.rb3 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][3],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=3,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="White")
        self.rb1.grid(row=4, sticky=W)
        self.rb1 = Radiobutton(self.quiz_frame,
                               text=questions_answers[qnum][4],
                               font=("Helvetica", "12"),
                               bg=background_color,
                               value=4,
                               padx=10,
                               pady=10,
                               variable=self.var1,
                               indicator=0,
                               background="White")
        self.rb1.grid(row=5, sticky=W)

        self.quiz_instance = Button(self.quiz_frame,
                                    text="Next",
                                    font=("Helvetica", "13", "bold"),
                                    bg="Green3")
        self.quiz_instance.grid(row=7, padx=5, pady=5)
        self.score_label = Label(
            self.quiz_frame,
            text="SCORE",
            font=("Arial", "10", "bold"),
            bg=background_color,
        )
        self.score_label.grid(row=8, padx=10, pady=1)

    def questions_setup(self):
        randomiser()
        self.var1.set(0)
        self.question_label.config(text=questions_answers[qnum][0])
        self.rb1.config(text=questions_answers[qnum][1])
        self.rb2.config(text=questions_answers[qnum][2])
        self.rb3.config(text=questions_answers[qnum][3])
        self.rb4.config(text=questions_answers[qnum][4])

    def test_progress(self):
        global score
        scr_label = self.score_label
        choice = self.var1.get()
        if len(asked) > 9:
            if choice == questions_answers[qnum][6]:
                score += 1
                scr_label.configure(text=score)
                self.quiz_instance.config(text="Confirm")

            else:
                score += 0
                scr_label.configure(text="The correct answer was: " +
                                    questions_answers[qnum][5])
                self.quiz_instance.config(text="Confirm")
                self.endscreen()
        else:
            if choice == 0:
                self.quiz._instance.config(
                    text=
                    "Try Again, You didn't select an option then submit again")
                choice = self.var1.get()
            else:
                if choice == questions_answers[qnum][6]:
                    score += 1
                    scr_label.configure(text=score)
                    self.quiz_instance.config(text="Next")
                    self.questions_setup()
                else:
                    score += 0
                    scr_label.configure(text="The correct answer was: " +
                                        questions_answers[qnum][5])
                    self.quiz_instance.config(text="Next")
                    self.questions_setup()


if __name__ == "__main__":
    root = Tk()
    root.title("CAR BRAND QUIZ")
    quiz_instance = QuizStarter(root)
    root.mainloop()





