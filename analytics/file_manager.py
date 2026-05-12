import os
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