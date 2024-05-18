from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):  # Ref-3
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Hello there",
            # To wrap text
            width=280,
            font=FONT,
            fill=THEME_COLOR
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Ref-2
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.chose_true, bd=0)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.chose_false, bd=0)
        self.false_button.grid(column=1, row=2)

        # Had to be called before mainloop otherwise it will execute only after the window is destroyed
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        # So we always get white bg on new question
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz")
            # Ref-5
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def chose_true(self):
        # Like this
        self.give_feedback(self.quiz.check_answer('True'))

    def chose_false(self):
        # Or this
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="spring green")
        else:
            self.canvas.config(bg="red")

        # Ref-4
        self.window.after(1000, func=self.get_next_question)



