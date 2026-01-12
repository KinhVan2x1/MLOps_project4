from typing import List, Dict

Student = Dict[str, float|str]

class Evaluator:
    def mean_absolute_error(self,
                            y_true: List[float],
                            y_pred: List[float]) -> float:
        if len(y_true) != len(y_pred):
            raise ValueError('y_true and y_pred must have the same length')
        
        errors = [
            abs(t - p) for t, p in zip(y_true, y_pred)
        ]
        
        return sum(errors)/len(errors)
    