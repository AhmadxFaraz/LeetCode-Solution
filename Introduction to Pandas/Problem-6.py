import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email")

if __name__ == "__main__":
    customers = pd.DataFrame([[1, "John", "john@example.com"], [2, "Doe", "john@example.com"], [3, "Jane", "jane@example.com"]], columns=["customer_id", "name", "email"])
    print(dropDuplicateEmails(customers))

    