import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from study_report import load_data, generate_student_report

def display_report():
    """Fetches the student report based on user input and displays it in the text area."""
    student_name = entry_student_name.get().strip()
    month = entry_month.get().strip()
    year = entry_year.get().strip()

    # Validate inputs
    if not student_name or not month or not year:
        messagebox.showwarning("Input Error", "Please enter all fields.")
        return

    try:
        # Convert month and year to integers
        month = int(month)
        year = int(year)
# the only human conde in this project
        if not (1 <= month <= 12):
            messagebox.showerror("Input Error", "Month should be between 1 and 12.")
            return
        if not (1900 <= year <= 2100):
            messagebox.showerror("Input Error", "Year should be between 1900 and 2100.")
            return

        # Load data and generate report
        data = load_data("study_hours.csv")
        if student_name not in data['Student'].values:
            messagebox.showerror("Student Not Found", f"No data available for student '{student_name}'.")
            return
        report = generate_student_report(data, student_name, year, month)

        # Display report in text area
        text_output.config(state="normal")
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, report)
        text_output.config(state="disabled")
    except ValueError:
        messagebox.showerror("Input Error", "Month and Year should be numbers.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "The CSV file could not be found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Study Hours Report Generator")
root.geometry("500x400")
root.configure(bg="#f4f4f9")

# Main Frame for Padding
main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Heading Label
label_heading = ttk.Label(main_frame, text="KTH Study Hours Report Generator", font=("Helvetica", 14, "bold"))
label_heading.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Labels and Entry fields
label_student_name = ttk.Label(main_frame, text="Student Name:")
label_student_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_student_name = ttk.Entry(main_frame, width=30)
entry_student_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")

label_month = ttk.Label(main_frame, text="Month (1-12):")
label_month.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_month = ttk.Entry(main_frame, width=10)
entry_month.grid(row=2, column=1, padx=5, pady=5, sticky="w")

label_year = ttk.Label(main_frame, text="Year:")
label_year.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_year = ttk.Entry(main_frame, width=10)
entry_year.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Generate Button
button_generate = ttk.Button(main_frame, text="Generate Report", command=display_report)
button_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Text area to display the output
text_output = tk.Text(main_frame, wrap="word", width=50, height=10, font=("Courier", 10), state="disabled", bg="#e6e8f0")
text_output.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

# Style and Layout Customization
style = ttk.Style(root)
style.configure("TLabel", font=("Helvetica", 10))
style.configure("TButton", font=("Helvetica", 10, "bold"))

# Run the application
root.mainloop()
