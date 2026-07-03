import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

if __name__ == "__main__":
    report_data = {
        'product': ['A', 'B', 'C'],
        'Q1': [100, 200, 300],
        'Q2': [150, 250, 350],
        'Q3': [200, 300, 400],
        'Q4': [250, 350, 450]
    }
    
    report = pd.DataFrame(report_data)
    report = meltTable(report)
    print(report)