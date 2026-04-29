import os
import csv
import json
#task a1
class FileManager:    
    def __init__(self, filename):
        self.filename = filename
    
    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False
    
    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")
        
        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")

    #task 2
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

    #task 3
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    
    def analyse(self):
        gpas = []
        high_performers_count = 0
        
        for student in self.students:
            try:
                gpa = float(student['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers_count += 1
            except ValueError:
                print(f"Warning: could not convert GPA value for student {student.get('student_id', 'unknown')} - skipping row.")
                continue
        
        if len(gpas) == 0:
            print("Error: No valid GPA data found.")
            self.result = {}
            return self.result
        
        avg_gpa = sum(gpas) / len(gpas)
        max_gpa = max(gpas)
        min_gpa = min(gpas)
        
        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(avg_gpa, 2),
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performers_count
        }
        
        return self.result
    
    def print_results(self):
        if not self.result:
            print("No results to print. Please run analyse() first.")
            return
        
        print("\n" + "-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"Total students : {self.result.get('total_students', 0)}")
        print(f"Average GPA : {self.result.get('average_gpa', 0)}")
        print(f"Highest GPA : {self.result.get('max_gpa', 0)}")
        print(f"Lowest GPA : {self.result.get('min_gpa', 0)}")
        print(f"Students GPA>3.5 : {self.result.get('high_performers', 0)}")
        print("-" * 30)
    #task 4
class ResultSaver:    
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    
    def save_json(self):
        try:
            output_dir = os.path.dirname(self.output_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            with open(self.output_path, "w", encoding="utf-8") as json_file:
                json.dump(self.result, json_file, indent=4)
            print(f"\nResult saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving JSON file: {e}")


def main():
    fm = FileManager('students.csv')
    
    if not fm.check_file():
        print('Stopping program.')
        return
    
    fm.create_output_folder()
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()

    print("\n" + "-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)
    
    try:
        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, dl.students))
        print(f"GPA > 3.8 : {len(high_gpa)}")
    except (ValueError, KeyError):
        print("Warning: Could not filter GPA > 3.8")
    
    try:
        gpa_values = list(map(lambda s: float(s['GPA']), dl.students))
        print(f"GPA values (first 5) : {gpa_values[:5]}")
    except (ValueError, KeyError):
        print("Warning: Could not map GPA values")
    
    try:
        hard_workers = list(filter(lambda s: float(s.get('study_hours_per_day', 0)) > 4, dl.students))
        print(f"study_hours_per_day > 4 : {len(hard_workers)}")
    except (ValueError, KeyError):
        print("Warning: Could not filter study hours")
    print("-" * 30)
if __name__ == "__main__":
    main()