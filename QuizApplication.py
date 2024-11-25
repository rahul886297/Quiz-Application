import tkinter as tk
from tkinter import messagebox

# Question data
questions = [
    {"question": "What is the capital of France?", 
     "options": ["Paris", "London", "Rome", "Berlin"], 
     "answer": "Paris"},
    {"question": "What is 2 + 2?", 
     "options": ["3", "4", "5", "6"], 
     "answer": "4"},
    {"question": "Who wrote 'Hamlet'?", 
     "options": ["Charles Dickens", "Mark Twain", "William Shakespeare", "J.K. Rowling"], 
     "answer": "William Shakespeare"},
    {"question": "What is the largest planet in our Solar System?", 
     "options": ["Earth", "Mars", "Jupiter", "Saturn"], 
     "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", 
     "options": ["H2O", "O2", "HO2", "H2"], 
     "answer": "H2O"},
    {"question": "Which country is known as the Land of the Rising Sun?", 
     "options": ["China", "Japan", "South Korea", "Thailand"], 
     "answer": "Japan"},
    {"question": "Who is known as the Father of Computers?", 
     "options": ["Charles Babbage", "Alan Turing", "Tim Berners-Lee", "Bill Gates"], 
     "answer": "Charles Babbage"},
    {"question": "What is the square root of 64?", 
     "options": ["6", "8", "10", "12"], 
     "answer": "8"},
    {"question": "Which element has the atomic number 1?", 
     "options": ["Oxygen", "Nitrogen", "Hydrogen", "Helium"], 
     "answer": "Hydrogen"},
    {"question": "What is the longest river in the world?", 
     "options": ["Amazon", "Nile", "Yangtze", "Mississippi"], 
     "answer": "Nile"}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        
        self.question_index = 0
        self.score = 0

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="center")
        self.question_label.pack(pady=20)
        
        # Options as radio buttons
        self.selected_option = tk.StringVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_option, font=("Arial", 12), value=f"Option{i}")
            rb.pack(anchor="w", padx=20, pady=5)
            self.radio_buttons.append(rb)
        
        # Next Button
        self.next_button = tk.Button(root, text="Next", command=self.next_question, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.next_button.pack(pady=20)

        # Initialize quiz
        self.display_question()

    def display_question(self):
        """Display the current question and options."""
        question_data = questions[self.question_index]
        self.question_label.config(text=question_data["question"])
        options = question_data["options"]
        for i, option in enumerate(options):
            self.radio_buttons[i].config(text=option, value=option)
        self.selected_option.set("")  # Reset selection

    def next_question(self):
        """Check the answer and move to the next question."""
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        # Check the answer
        if selected == questions[self.question_index]["answer"]:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect!", f"The correct answer is: {questions[self.question_index]['answer']}")

        # Move to the next question or end the quiz
        self.question_index += 1
        if self.question_index < len(questions):
            self.display_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        """Show the final score and close the application."""
        messagebox.showinfo("Quiz Completed", f"Your final score is {self.score}/{len(questions)}!")
        self.root.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
