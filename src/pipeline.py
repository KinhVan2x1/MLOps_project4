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

        # Train split test
        train_data, validation_data = self.loader.train_test_split(processed_data, split_ratio=0.5)
    
        # Model training
        self.model.fit(train_data)

        # Model Prediction
        predictions = []
        for row in train_data:
            predicted_score = self.model.predict(row['study_hours'])
            predictions.append(predicted_score)
        return predictions
        
       
        

        