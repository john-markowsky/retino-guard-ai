from scipy.io import arff
import pandas as pd

data = arff.loadarff(r'/home/jgm/Documents/intelligent-systems-project/messidor_features.arff')

df = pd.DataFrame(data)

print(df)
