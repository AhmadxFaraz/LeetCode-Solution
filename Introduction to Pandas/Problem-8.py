import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"]*2
    return employees

if __name__=="__main__":
    employees = pd.DataFrame([[1, "John", 50000], [2, "Alice", 60000], [3, "Bob", 70000], [4, "Eve", 80000]], columns=["employee_id", "name", "salary"])
    print(modifySalaryColumn(employees))