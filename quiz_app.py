import tkinter as tk
from tkinter import messagebox

# Quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest mammal?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "answer": "Blue Whale"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")
        self.q_index = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", wraplength=350, font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.options = []
        self.var = tk.StringVar()

        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Helvetica", 12))
            rb.pack(anchor="w", padx=20)
            self.options.append(rb)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.q_index < len(questions):
            q = questions[self.q_index]
            self.question_label.config(text=f"Q{self.q_index + 1}: {q['question']}")
            self.var.set(None)
            for i, option in enumerate(q["options"]):
                self.options[i].config(text=option, value=option)
        else:
            self.show_result()

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No selection", "Please select an answer.")
            return
        correct = questions[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct answer was: {correct}")
        self.q_index += 1
        self.load_question()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your score: {self.score} out of {len(questions)}")
        self.root.quit()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
