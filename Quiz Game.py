import tkinter as tk

questions = ("What is the capital of Australia?: ",
              "Who painted the Mona Lisa?: ",
              "What is the largest country in the world by land area?: ",
              "What is the chemical symbol for gold?: ",
              "In what year did World War II end?: ",
              "Who was the first president of the United States?: ",
              "What is the largest ocean on Earth?: ",
              "What is the currency of Japan?: ")

options = (("A. Canberra", "B. Sydney", "C. Melbourne", "D. Brisbane"),
           ("A. Pablo Picasso", "B. Leonardo da Vinci", "C. Salvador Dalí", "D. Vincent van Gogh"),
           ("A. Canada", "B. China", "C. Russia", "D. Denmark"),
           ("A. Au", "B. Ga ", "C. Ge", "D. Gd"),
           ("A. 1941", "B. 1942", "C. 1943", "D. 1945"),
           ("A. John Adams", "B. Thomas Jefferson", "C. Andrew Jackson", "D. George Washington"),
           ("A. Atlantic", "B. Pacific", "C. Indian", "D. Artic"),
           ("A. Yuan", "B. Yen", "C. Rial ", "D. Won"))

answers = ("A", "B", "C", "A", "D", "D", "B", "B")

class QuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("400x300")

        self.question_label = tk.Label(self, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        question = questions[self.current_question]
        self.question_label.config(text=question)

        for i in range(4):
            self.option_buttons[i].config(text=options[self.current_question][i])

    def check_answer(self, index):
        if chr(ord('A') + index) == answers[self.current_question]:
            self.result_label.config(text="Correct!")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrect. The correct answer is {answers[self.current_question]}")

        self.current_question += 1
        if self.current_question < len(questions):
            self.show_question()
        else:
            self.result_label.config(text=f"Quiz completed. Your score is {self.score}/{len(questions)}")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()