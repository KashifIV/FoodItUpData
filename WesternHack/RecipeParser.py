import pandas as pd 
import numpy as np 


food = set()
with open('foodItems.txt') as file: 
    for line in file: 
        food.add(line.lower().strip('\n'))
filename = 'epi_r.csv'

data = pd.read_csv(filename)
recipes = set()

for x in data.columns: 
    if not (x.lower() in food): 
        data.drop(x, axis = 1, inplace = True)



for x in data.title: 
    if x in recipes: 
        print(x)
    else: 
        recipes.add(x)

print("Done")

