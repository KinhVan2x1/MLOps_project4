from typing import List, Dict

Student = Dict[str, float| str]

class Preprocessor:
    def clean(self, data: List[Student]) -> List[Student]:
        cleaned: List[Student] = []

        for student in data:
            math_score = student.get('math_score')
            study_hours = student.get('study_hours')

            # Drop invalid rows
            if math_score is None or study_hours is None or study_hours == 0:
                continue
            
            # Feature engineering
            student['score_per_hour'] = math_score/study_hours
            cleaned.append(student)
        return cleaned
    
    def train_test_split(self,students_data: List[Student], split_ratio:float = 0.8):
        split = int(len(students_data) * split_ratio)
        return students_data[:split], students_data[split:]
