import unittest
import pandas as pd
from datetime import datetime
from study_report import load_data, filter_by_month, generate_report
import io
import sys

SAMPLE_DATA = pd.DataFrame({
    'Student': ['Student A', 'Student A', 'Student B', 'Student B', 'Student A'],
    'Subject': ['Mathematics', 'Physics', 'Computer Science', 'Biology', 'Computer Science'],
    'Date': [datetime(2023, 10, 1), datetime(2023, 10, 2), datetime(2023, 10, 1), datetime(2023, 10, 2), datetime(2023, 10, 4)],
    'Hours': [2.0, 1.5, 3.0, 2.0, 2.0]
})


class TestLoadData(unittest.TestCase):
    def test_load_data_success(self):
        """Test that data loads correctly when a valid CSV path is given."""
        data = load_data("study_hours.csv")  # Use the real path or mock it
        self.assertIsNotNone(data, "Data should not be None.")
        self.assertTrue(isinstance(data, pd.DataFrame), "Data should be a DataFrame.")
    
    def test_load_data_file_not_found(self):
        """Test the load_data function with a non-existent file."""
        data = load_data("nonexistent_file.csv")
        self.assertIsNone(data, "Data should be None when the file does not exist.")

# test filter_by_month funtion
class TestFilterByMonth(unittest.TestCase):
    def test_filter_by_month(self):
        """Test filtering data by a specific month."""
        filtered_data = filter_by_month(SAMPLE_DATA, 2023, 10)
        self.assertEqual(len(filtered_data), 5, "There should be 5 records for October 2023.")
        self.assertTrue(all(filtered_data['Date'].dt.month == 10), "All records should be from October.")
        self.assertTrue(all(filtered_data['Date'].dt.year == 2023), "All records should be from 2023.")



# test generate_report function
class TestGenerateReport(unittest.TestCase):
    def test_generate_report_output(self):
        """Test that the report is generated with correct output for each student."""
        captured_output = io.StringIO()  # Create a buffer to capture output
        sys.stdout = captured_output     # Redirect stdout to the buffer

        generate_report(SAMPLE_DATA, "2023-10")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Check the output content
        output = captured_output.getvalue()
        self.assertIn("Study Hours Report for \"Student A\" for the month of \"2023-10\":", output)
        self.assertIn("Mathematics: 2.0 hours", output)
        self.assertIn("Physics: 1.5 hours", output)
        self.assertIn("Total Study Hours: 5.5 hours", output)
        self.assertIn("Study Hours Report for \"Student B\" for the month of \"2023-10\":", output)
        self.assertIn("Computer Science: 3.0 hours", output)
        self.assertIn("Biology: 2.0 hours", output)
        self.assertIn("Total Study Hours: 5.0 hours", output)


#test the completer workflow
class TestFullWorkflow(unittest.TestCase):
    def test_full_workflow(self):
        """Test loading, filtering, and generating a report in a complete workflow."""
        data = load_data("study_hours.csv")
        if data is not None:
            data_filtered = filter_by_month(data, 2023, 10)
            generate_report(data_filtered, "2023-10")
