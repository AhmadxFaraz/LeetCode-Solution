import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    result = students.loc[students["student_id"]==101]
    return result.iloc[:,1:]

if __name__ == "__main__":
    students = pd.DataFrame([[1, "John", 25], [2, "Alice", 30], [101, "Bob", 28], [4, "Eve", 35]], columns=["student_id", "name", "age"])
    print(selectData(students))