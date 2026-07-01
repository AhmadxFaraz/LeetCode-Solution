import pandas as pd

def getDataframeSize(players: pd.DataFrame):
    return list(players.shape)

if __name__ == "__main__":
    players = pd.DataFrame([[1, 20], [2, 21], [3, 22]], columns=["player_id", "age"])
    print(getDataframeSize(players))