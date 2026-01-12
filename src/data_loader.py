from typing import List, Dict
import csv

Student = Dict[str, float | str]

class DataLoader:
    def __init__(self, path):
        self.path = path

    def load(self) -> List[Student]:
        students: List[Student] = []
        with open(self.path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                student: Student = {
                    'name': row['name'],
                    "math_score": float(row["math_score"]) if row["math_score"] else None,
                    'study_hours': float(row['study_hours']) if row['study_hours'] else None,
                }
                students.append(student)
        return students
    
    def train_test_split(self,students_data: List[Student], split_ratio:float = 0.8):
        split = int(len(students_data) * split_ratio)
        return students_data[:split], students_data[split:]
