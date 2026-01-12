from src.data_loader import DataLoader

def test_train_test_split():
    loader = DataLoader(path="dummy.csv")  # path not used

    students = [
        {"name": "Alice", "math_score": 85.0, "study_hours": 10.0},
        {"name": "Bob", "math_score": 60.0, "study_hours": 3.0},
        {"name": "Charlie", "math_score": 90.0, "study_hours": 12.0},
        {"name": "Daisy", "math_score": 70.0, "study_hours": 6.0},
        {"name": "Ethan", "math_score": 55.0, "study_hours": 4.0},
    ]

    train, test = loader.train_test_split(students, split_ratio=0.8)

    print("Train data:", train)
    print("Test data:", test)

    # Simple checks
    assert len(train) == 4, "Train set should have 4 students"
    assert len(test) == 1, "Test set should have 1 student"

    print("✅ train_test_split works correctly!")

if __name__ == "__main__":
    test_train_test_split()