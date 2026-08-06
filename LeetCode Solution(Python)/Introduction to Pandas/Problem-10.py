import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

if __name__ == "__main__":
    students = pd.DataFrame([[1, "John", 25, 85.5], [2, "Alice", 30, 90.0], [3, "Bob", 28, 78.0]], columns=["student_id", "name", "age", "grade"])
    print(changeDatatype(students))