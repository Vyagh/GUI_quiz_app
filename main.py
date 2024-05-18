from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# Ref-1
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")





# NOTES:
# Everything works Fine But simple symbols like ' or " are still encoded.
# In HTML certain characters are reserved so if we use them we have to convert them to HTML entities to resolve any
#   conflicts with the HTML code:
#   https://www.w3schools.com/html/html_entities.asp

# This is added functionality:
# unescaped_text = html.unescape(self.current_question.text)

# Ref-1
# Had to comment this while block because mainloop gets confused when some other loop is near it.-General Guideline

# Ref-2
# hm self. use krte hai class ke andr so we can access that property kahi bhi inside our class but we don't have to use
#   it with everything e.g. we don't want to access images of button anywhere so unhe self. nhi kiya.

# Ref-3
# We had to explicitly tell about the Type of quiz_brain as QuizBrain instance to help us and others with readability
#   and also for my IDE to show me available methods for self.quiz. object, It also raises error now if I pass something
#   other than a QuizBrain Instance to my quiz_ui therefore helping us.
#     It's basically called TYPE HINTS (Helps us to read and know code better)

# Wrap text using width param

# Ref-4 (ui)
# Do not use time.sleep(1000) as it messes up with mainloop so instead use window.after

# On getting to last question after than it gives us list index out of range error.
# Disabling Buttons in the end

# Ref-5 (ui)
# To disable buttons
# .config(state="disabled")