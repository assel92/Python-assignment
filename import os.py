import os
import csv
import json

def main():
    # Task A1 — Check File and Create Output Folder
    print("Checking file...")
    
    # Показываем текущую папку
    current_dir = os.getcwd()
    print(f"Текущая папка: {current_dir}")
    
    # Проверяем все файлы в папке
    print("\nВсе файлы в папке:")
    all_files = os.listdir('.')
    for file in all_files:
        print(f"  - {file}")
    
    # Ищем students.csv
    filename = "students.csv"
    
    if not os.path.exists(filename):
        print(f"\nError: {filename} not found!")
        
        # Ищем похожие файлы
        csv_files = [f for f in all_files if f.endswith('.csv')]
        if csv_files:
            print(f"\nНайденные CSV файлы: {csv_files}")
            print("Возможно, файл называется по-другому. Используйте одно из этих имен:")
            for f in csv_files:
                print(f"  - {f}")
        else:
            print("CSV файлы не найдены в текущей папке.")
        return
    
    print(f"File found: {filename}")
    
    print("\nChecking output folder...")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")
    
    # Task A2 — Read CSV and Preview Data
    students = []
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students = list(reader)
    except Exception as e:
        print(f"Ошибка при открытии файла: {e}")
        return
    
    print(f"\nTotal students: {len(students)}")
    print("First 5 rows:")
    print("-" * 30)
    
    for i in range(min(5, len(students))):
        student = students[i]
        print(f"{student['student_id']} | {student['age']} | {student['gender']} | {student['country']} | GPA: {student['GPA']}")
    
    print("-" * 30)
    
    # Task A3 — GPA Analysis
    gpas = []
    high_performers_count = 0
    
    for student in students:
        gpa = float(student['GPA'])
        gpas.append(gpa)
        if gpa > 3.5:
            high_performers_count += 1
    
    avg_gpa = sum(gpas) / len(gpas)
    max_gpa = max(gpas)
    min_gpa = min(gpas)
    
    print("\n" + "-" * 30)
    print("GPA Analysis")
    print("-" * 30)
    print(f"Total students : {len(students)}")
    print(f"Average GPA : {round(avg_gpa, 2)}")
    print(f"Highest GPA : {max_gpa}")
    print(f"Lowest GPA : {min_gpa}")
    print(f"Students GPA>3.5 : {high_performers_count}")
    print("-" * 30)
    
    # Task A4 — Save Results to JSON and Print Summary
    result = {
        "analysis": "GPA Statistics",
        "total_students": len(students),
        "average_gpa": round(avg_gpa, 2),
        "max_gpa": max_gpa,
        "min_gpa": min_gpa,
        "high_performers": high_performers_count
    }
    
    with open("output/result.json", "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4)
    
    print("\n" + "=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print(f"Analysis : {result['analysis']}")
    print(f"Total students : {result['total_students']}")
    print(f"Average GPA : {result['average_gpa']}")
    print(f"Highest GPA : {result['max_gpa']}")
    print(f"Lowest GPA : {result['min_gpa']}")
    print(f"High performers : {result['high_performers']}")
    print("=" * 30)
    print("Result saved to output/result.json")

if __name__ == "__main__":
    main()