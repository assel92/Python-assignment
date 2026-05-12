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
        print("\n" + "=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        
        for key, value in self.result.items():
            print(f"{key}: {value}")
        
        print("=" * 30)

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
