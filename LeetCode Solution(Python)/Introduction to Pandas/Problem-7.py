import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[~students["name"].isnull()]

if __name__ == "__main__":
    students = pd.DataFrame([[1, "John", 25], [2, None, 30], [101, None, 28], [4, "Eve", None]], columns=["student_id", "name", "age"])
    print(students)
    print(dropMissingData(students))