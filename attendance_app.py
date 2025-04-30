import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from datetime import datetime

# Sample list of students
students = ["Alice", "Bob", "Charlie", "David", "Emma"]

# CSV file name
FILENAME = "attendance_records.csv"

# Create file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Student Name", "Status"])

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("University Attendance App")
        self.root.geometry("400x300")

        # Title
        tk.Label(root, text="University Attendance System", font=("Helvetica", 14)).pack(pady=10)

        # Student dropdown
        tk.Label(root, text="Select Student:").pack()
        self.student_var = tk.StringVar()
        self.student_combo = ttk.Combobox(root, textvariable=self.student_var, values=students)
        self.student_combo.pack(pady=5)

        # Attendance status radio buttons
        tk.Label(root, text="Status:").pack()
        self.status_var = tk.StringVar(value="Present")
        tk.Radiobutton(root, text="Present", variable=self.status_var, value="Present").pack()
        tk.Radiobutton(root, text="Absent", variable=self.status_var, value="Absent").pack()

        # Mark attendance button
        tk.Button(root, text="Mark Attendance", command=self.mark_attendance, bg="green", fg="white").pack(pady=10)

        # View attendance button
        tk.Button(root, text="View Attendance Records", command=self.view_attendance).pack(pady=5)

    def mark_attendance(self):
        name = self.student_var.get()
        status = self.status_var.get()
        date = datetime.now().strftime("%Y-%m-%d")

        if not name:
            messagebox.showwarning("Input Error", "Please select a student.")
            return

        # Append to CSV
        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, name, status])

        messagebox.showinfo("Success", f"Attendance marked for {name} as {status}.")

    def view_attendance(self):
        # Read and display attendance file
        if not os.path.exists(FILENAME):
            messagebox.showinfo("No Records", "No attendance records found.")
            return

        with open(FILENAME, "r") as file:
            records = file.read()

        view_window = tk.Toplevel(self.root)
        view_window.title("Attendance Records")
        text = tk.Text(view_window, wrap="none")
        text.insert("1.0", records)
        text.pack(expand=True, fill="both")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
