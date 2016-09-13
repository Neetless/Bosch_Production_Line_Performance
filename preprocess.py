import pandas as pd

train_numeric_file = './input/train_numeric.csv.zip'

train_numeric = pd.read_csv(train_numeric_file, compression='zip')

print(train_numeric.head())
