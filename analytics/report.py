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