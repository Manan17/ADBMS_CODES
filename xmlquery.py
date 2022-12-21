import pandas as pd
data = pd.read_xml('database.xml')
print(data[data['age']>18])