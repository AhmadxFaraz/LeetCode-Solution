import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    result =  animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)
    return result[["name"]]

if __name__ == "__main__":
    data = {
        'name': ['Elephant', 'Tiger', 'Dog', 'Cat'],
        'weight': [1200, 220, 30, 10]
    }
    
    animals_df = pd.DataFrame(data)
    heavy_animals = findHeavyAnimals(animals_df)
    print(heavy_animals)