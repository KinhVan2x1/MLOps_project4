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
