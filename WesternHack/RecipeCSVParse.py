import pandas as pd
import numpy as np 
import json as json

filename = 'allrecipes-recipes.json'

data = []

with open(filename) as file: 
    for line in file: 
        d = json.loads(line)
        data.append(d)

dataframe = pd.DataFrame() 
for x in data:
    item = pd.DataFrame.from_dict(x, orient='index')
    item = item.transpose()
    dataframe = dataframe.append(item, ignore_index=True)


print(dataframe.columns)

similar = [] 
nutritionTitles = set()

nutritionFile = 'epi_r.csv'
data = pd.read_csv(nutritionFile)

for x in data.title: 
    nutritionTitles.add(x.lower())

for x in data.title: 
    if (x.lower() in nutritionTitles): 
        similar.append(x.lower())
print(len(similar))