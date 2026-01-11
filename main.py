
from src.pipeline import TrainingPipeline

# File path 
path = 'data/raw/students.csv'

# # Parameters
# study_hours = 5

def main() -> None:
    # Pipeline initiation
    pipeline = TrainingPipeline(path)
    results = pipeline.run()

    for row in results:
        print(row)

if __name__ == '__main__':
    main()
