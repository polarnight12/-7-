import pandas as pd
data = pd.read_csv('test.csv')
print(data)
data['价格'][data['价格'] > 1000] = None
print(data.dropna())
data['价格'][data['价格'] > 1000] = None
print(data.fillna(data.mean()))


