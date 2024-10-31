import pandas as pd

def load_data(file_path):
    """Loads the study hours data from a CSV file."""
    return pd.read_csv(file_path, parse_dates=['Date'])

def filter_by_month(data, year, month):
    """Filters data for a specific year and month."""
    return data[(data['Date'].dt.year == year) & (data['Date'].dt.month == month)]

def generate_report(data):
    """Generates a study hours report for the provided data."""
    report = ""
    total_hours = 0

    # Group by subject and calculate total hours per subject
    for subject, group in data.groupby("Subject"):
        subject_hours = group["Hours"].sum()
        report += f"{subject}: {subject_hours} hours.\n"
        total_hours += subject_hours
    
    report += f"Total Study Hours: {total_hours} hours"
    return report

def generate_student_report(data, student_name, year, month):
    """Generates a study report for a specific student, year, and month."""
    # Filter data by student name
    student_data = data[data['Student'] == student_name]
    
    # Filter data by month and year
    monthly_data = filter_by_month(student_data, year, month)
    
    # Generate the report if there's data available for the student
    if not monthly_data.empty:
        report = generate_report(monthly_data)
        return f"\nStudy Hours Report for {student_name} for {year}-{month:02}:\n{report}"
    else:
        return f"No data available for {student_name} in {year}-{month:02}."

if __name__ == "__main__":
    # Load data
    data = load_data("study_hours.csv")
    
    # Define student name, year, and month for the report
    student_name = "Student B"  # You can change this to any student's name in your data
    year = 2023
    month = 10

    # Generate and print the report
    report = generate_student_report(data, student_name, year, month)
    print(report)
