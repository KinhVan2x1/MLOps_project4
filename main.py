
from src.pipeline import TrainingPipeline
from src.evaluator import Evaluator

# File path 
path = 'data/raw/students.csv'

# # Parameters
# study_hours = 5

def main() -> None:
    # Pipeline initiation
    pipeline = TrainingPipeline(path)
    results = pipeline.run()

    # Print result
    print(results)
    # mae = Evaluator.mean_absolute_error(y_pred=results, y_true=)

if __name__ == '__main__':
    main()
