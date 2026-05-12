import os
import csv
import json
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
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    
    def analyse(self):
        print("Not implemented - use a child class")
    
    def print_results(self):
        print("\n" + "=" * 30)
        for key, value in self.result.items():
            print(f"{key}: {value}")
        print("=" * 30)
    
    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"

class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)
    
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
    
    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"
    def print_results(self):
        """Override print_results with header and footer, calling super().print_results()"""
        print("\n" + "=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        
        # Call base class print_results to print key-value pairs
        for key, value in self.result.items():
            print(f"{key}: {value}")
        
        print("=" * 30)

class Report:
    def __init__(self, analyser, saver):
        self.analyser = analyser 
        self.saver = saver      
    
    def generate(self):
        print("\n" + "-" * 30)
        print("Generating report...")
        print("-" * 30)
        self.analyser.analyse()
        self.analyser.print_results()
        self.saver.save_json()
        print("Report complete.")

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

def polymorphism_demo(students_full, students_sample):
    print("\n" + "=" * 50)
    print("Task 5: Polymorphism")
    print("=" * 50)
    class CountryAnalyser(DataAnalyser):
        def __init__(self, students):
            super().__init__(students)
        
        def analyse(self):
            country_counts = {}
            for student in self.students:
                country = student.get('country', 'Unknown')
                country_counts[country] = country_counts.get(country, 0) + 1
            
            top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
            
            self.result = {
                "total_students": len(self.students),
                "total_countries": len(country_counts),
                "top_3": top_3
            }
            return self.result
        
        def __str__(self):
            return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
        
        def print_results(self):
            print("\n" + "=" * 30)
            print("COUNTRY ANALYSIS REPORT")
            print("=" * 30)
            for key, value in self.result.items():
                print(f"{key}: {value}")
            print("=" * 30)
    
    analysers = [
        GpaAnalyser(students_full),
        CountryAnalyser(students_sample)  
    ]
    
    print("\nRunning all analysers:")
    print("-" * 40)
    
    for a in analysers:
        print(a)           
        a.analyse()        
        a.print_results()  
        print()

def main():
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        return
    
    fm.create_output_folder()
    
    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()
    
    sample_students = dl.students[:100] 
    
    polymorphism_demo(dl.students, sample_students)
    

    analyser = GpaAnalyser(dl.students)
    saver = ResultSaver(analyser.result, 'output/result.json')
    report = Report(analyser, saver)
    report.generate()
    
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