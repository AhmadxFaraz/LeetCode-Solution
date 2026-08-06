import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.fillna({"quantity": 0}, inplace=True)
    return products

if __name__ == "__main__":
    products = pd.DataFrame([[1, "Apple", 10], [2, "Banana", None], [3, "Orange", 5], [4, "Grapes", None]], columns=["product_id", "name", "quantity"])
    print(fillMissingValues(products))