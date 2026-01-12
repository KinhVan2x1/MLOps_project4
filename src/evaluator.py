from typing import List, Dict

Student = Dict[str, float|str]

class Evaluator:
    def mean_absolute_error(self,
                            y_true: List[float],
                            y_pred: List[float]) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError('y_true and y_pred must have the same length')
        
        errors = [abs(t - p) for t, p in zip(y_true, y_pred)]
        
        return sum(errors)/len(errors)

# # Test:

# evaluator = Evaluator()

# y_true = [10.0, 20.0, 30.0]
# y_pred = [12.0, 18.0, 33.0]

# result = evaluator.mean_absolute_error(y_true, y_pred)

# print(result)



    
