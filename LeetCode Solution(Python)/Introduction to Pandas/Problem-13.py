import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(weather, index="month", columns="city", values="temperature")

if __name__== "__main__":
    data = {
        'month': ['Jan', 'Jan', 'Feb', 'Feb'],
        'city': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
        'temperature': [30, 60, 32, 65]
    }
    
    weather_df = pd.DataFrame(data)
    pivoted_weather = pivotTable(weather_df)
    print(pivoted_weather)