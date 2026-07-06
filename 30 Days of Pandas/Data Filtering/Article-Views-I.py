import pandas as pd
import numpy as np

data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'], [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype({'article_id':'Int64', 'author_id':'Int64', 'viewer_id':'Int64', 'view_date':'datetime64[ns]'})

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    lis = []
    for i in range(len(views)):
        if views.iloc[i]['author_id'] == views.iloc[i]['viewer_id']:
            lis.append(views.iloc[i]['author_id'])
    lis = set(lis)
    lis = list(lis)
    lis = np.array(lis)
    lis.sort()
    lis = pd.DataFrame(lis,columns=['id'])
    return lis

# Second Approach
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    lis = views[views['author_id'] == views['viewer_id']]['author_id'].unique()
    lis = np.array(lis)
    lis.sort()
    lis = pd.DataFrame(lis,columns=['id'])
    return lis


print(article_views(views))