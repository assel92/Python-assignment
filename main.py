import os
import sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser

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
    print("\n" + "=" * 50)
    print("Task 5: Polymorphism")
    print("=" * 50)
    
    analysers = [
        GpaAnalyser(dl.students),
        CountryAnalyser(sample_students)
    ]
    
    print("\nRunning all analysers:")
    print("-" * 40)
    
    for a in analysers:
        print(a)
        a.analyse()
        a.print_results()
        print()
    
 
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