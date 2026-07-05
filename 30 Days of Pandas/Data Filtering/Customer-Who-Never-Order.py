import pandas as pd

data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})
data = [[1, 3], [2, 1]]
orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id':'Int64', 'customerId':'Int64'})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])]    
    # rename name clumn as customers
    result["customers"] = result["name"]
    result = result.drop(columns=["name"])
    result = result.drop(columns=["id"])
    return result

print(find_customers(customers, orders))