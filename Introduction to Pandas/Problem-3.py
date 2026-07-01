import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3, :]
    # or return employees.head(3)

if __name__ == "__main__":
    employees = pd.DataFrame([[1, "John", 25], [2, "Alice", 30], [3, "Bob", 28], [4, "Eve", 35]], columns=["employee_id", "name", "age"])
    print(selectFirstRows(employees))


