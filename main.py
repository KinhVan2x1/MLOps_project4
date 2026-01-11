from src.data_loader import DataLoader
from src.preprocessor import Preprocessor

path = 'data/raw/students.csv'

def main() -> None:
    loader = DataLoader(path)
    raw_data = loader.load()

    preprocessor = Preprocessor()
    clean_data = preprocessor.clean(raw_data)

    print(clean_data)

if __name__ == '__main__':
    main()
