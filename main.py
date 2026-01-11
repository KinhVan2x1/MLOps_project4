from src.data_loader import DataLoader
from src.preprocessor import Preprocessor
from src.model import StudyModel

path = 'data/raw/students.csv'

def main() -> None:
    # Load data
    loader = DataLoader(path)
    raw_data = loader.load()

    # Data Processing, Data Cleaning -> Need to add Data Versioning (DVC)
    preprocessor = Preprocessor()
    clean_data = preprocessor.clean(raw_data)

    # Fit data into model:
    model = StudyModel()
    model.fit(clean_data)
    
    # Prediction
    study_hours = 5
    pred = model.predict(study_hours)
    print(f'Predicted score for {study_hours} hours study: {pred}')

if __name__ == '__main__':
    main()
