# The model job is to: 
# 1. Learn parameters
# 2. Store them
# 3. Use them for prediction

# Define model's responsibility
# - Learn from processed data
# - Predict values for new data

# Design interface first:
# fit(data) → learn parameters
# fit(self, data: List[Student]) -> None

# predict(hours) → number
# predict(self, study_hours: float) -> float

from typing import List, Dict
Student= Dict[str, float | str]

class StudyModel:
    def __init__(self) -> None:
        self.average_score_per_hour: float| None = None
    
    def fit(self, data: List[Student]) -> None:
        ratios = []
        for row in data:
            ratios.append(row['score_per_hour'])
        
        self.average_score_per_hour = sum(ratios)/len(ratios)

    def predict(self, study_hours: float) -> float:
        if self.average_score_per_hour is None:
            raise ValueError("Model has not been trained yet")
        
        return study_hours * self.average_score_per_hour




