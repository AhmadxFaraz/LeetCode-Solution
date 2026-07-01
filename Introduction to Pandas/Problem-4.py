import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    pass

if __name__ == "__main__":
    students = pd.DataFrame([[1, "John", 25], [2, "Alice", 30], [3, "Bob", 28], [4, "Eve", 35]], columns=["student_id", "name", "age"])
    print(students)
    print(selectData(students))