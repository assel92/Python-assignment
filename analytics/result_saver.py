import os
import json

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