import csv
class DataLoader:    
    def __init__(self, filename):
        self.filename = filename
        self.students = []
    
    def load(self):
        print("\nLoading data...")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []
        except Exception as e:
            print(f"Error loading file: {e}")
            return []
    
    def preview(self, n=5):
        if not self.students:
            print("No data to preview. Please load data first.")
            return
        
        print(f"\nFirst {n} rows:")
        print("-" * 30)
        
        for i in range(min(n, len(self.students))):
            student = self.students[i]
            print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
        
        print("-" * 30)