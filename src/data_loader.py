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
    
