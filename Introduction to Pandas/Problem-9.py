import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={"id":"student_id", "first":"first_name", "last":"last_name", "age":"age_in_years"})

if __name__ == "__main__":
    students = pd.DataFrame([[1, "John", "Doe", 25], [2, "Alice", "Smith", 30], [3, "Bob", "Johnson", 28]], columns=["id", "first", "last", "age"])
    print(renameColumns(students))