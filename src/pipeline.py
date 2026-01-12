from typing import List, Dict
from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.model import StudyModel
from src.evaluator import Evaluator

Student = Dict[str, float| str]

class TrainingPipeline:
    def __init__(self, data_path: str):
        self.data_path = data_path  
        self.loader = DataLoader(data_path)
        self.preprocessor = Preprocessor()
        self.model = StudyModel()
        self.evaluator = Evaluator()
    
    def run(self) -> List[Student]:
        # Load Data
        raw_data = self.loader.load()

        # Process Data, Data Cleaning
        processed_data = self.preprocessor.clean(raw_data)
    
        # Model training
        self.model.fit(processed_data)

        # Model Prediction
        predictions = []
        for row in processed_data:
            predicted_score = self.model.predict(row['study_hours'])
            predictions.append(predicted_score)
        return predictions
        
       
        

        