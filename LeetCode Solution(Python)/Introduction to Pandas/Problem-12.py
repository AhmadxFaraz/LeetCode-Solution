import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2], axis=0, ignore_index=True)

if __name__== "__main__":
    # Example usage
    data1 = {'A': [1, 2], 'B': [3, 4]}
    data2 = {'A': [5, 6], 'B': [7, 8]}
    
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    print(concatenateTables(df1,df2))