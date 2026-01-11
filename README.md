# Mini MLOps Project: Student Performance Pipeline

This project is a **small, offline MLOps-style pipeline** designed for learning purposes. It focuses on **clean Python structure, OOP, type hints, and reproducibility**, without using APIs, Docker, or deployment tools.

The goal is to understand how real ML systems are **structured**, not just how models are trained.

---

## 🎯 Project Goals

* Practice **object-oriented programming (OOP)** in Python
* Understand **data pipelines** (load → clean → train → evaluate)
* Learn **type hints** and clean interfaces
* Think in terms of **artifacts** (models, metrics)
* Build foundations for future MLOps tools (MLflow, DVC, Airflow, etc.)

---

## 📁 Project Structure

```text
MLOps_project4/
├── data/
│   └── raw/
│       └── students.csv
├── artifacts/
│   ├── model.json
│   └── metrics.json
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── model.py
│   ├── evaluator.py
│   └── pipeline.py
├── .gitignore
├── main.py
└── README.md
```

---

## 🧠 Pipeline Overview

This project mimics a real ML training pipeline:

1. **Data Loading**
   Reads raw CSV data and converts it into typed Python objects.

2. **Preprocessing**

   * Removes invalid rows (missing values)
   * Performs feature engineering

3. **Model Training**
   Learns a simple parameter from the processed data (no ML libraries yet).

4. **Evaluation**
   Computes metrics to assess model quality.

5. **Artifacts**
   Saves trained model parameters and evaluation metrics to disk.

---

## 🧩 Components

### `DataLoader`

* Reads `students.csv`
* Converts data to Python dictionaries
* Handles missing values explicitly

### `Preprocessor`

* Drops invalid rows
* Creates new features (`score_per_hour`)

### `StudyModel`

* Mimics `fit()` / `predict()` behavior
* Learns average score per study hour
* Saves model parameters as JSON

### `Evaluator`

* Computes evaluation metrics (e.g. mean absolute error)

### `TrainingPipeline`

* Orchestrates all steps
* Ensures reproducibility
* Produces artifacts

---

## 📊 Example Data

`students.csv`

```csv
name,math_score,study_hours
Alice,85,10
Bob,60,3
Charlie,90,12
Daisy,,5
```

---

## ▶️ How to Run

From the project root:

```bash
python main.py
```

Expected output:

* Cleaned data printed to console
* Model saved to `artifacts/model.json`
* Metrics saved to `artifacts/metrics.json`

---

## 🧪 Example Output (After Preprocessing)

```python
[
 {'name': 'Alice', 'math_score': 85.0, 'study_hours': 10.0, 'score_per_hour': 8.5},
 {'name': 'Bob', 'math_score': 60.0, 'study_hours': 3.0, 'score_per_hour': 20.0},
 {'name': 'Charlie', 'math_score': 90.0, 'study_hours': 12.0, 'score_per_hour': 7.5}
]
```

---

## 🔍 Design Principles

* **Separation of concerns**: each class has one responsibility
* **Explicit typing**: improves readability and correctness
* **Reproducibility**: same input → same output
* **No magic**: standard library only

---

## 🚀 Future Extensions

This project can later be extended with:

* Pandas & scikit-learn
* MLflow or DVC for experiment tracking
* Logging instead of print statements
* Unit tests
* Docker & deployment

---

## 🧠 Learning Outcome

If you understand and can modify this project, you have a **strong foundation** for:

* Machine Learning pipelines
* MLOps system design
* Reading and writing production-grade Python

---

## 📌 Notes

* `__pycache__/` and `venv/` are ignored via `.gitignore`
* `.gitignore` and `__init__.py` are tracked intentionally

---

Happy learning 🚀
