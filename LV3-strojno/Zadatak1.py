import pandas as pd
import numpy as np

mtcars = pd.read_csv("C:\\Users\\Ivana\\Desktop\\LV3-strojno\\mtcars.csv")

print(mtcars[['car','mpg']].sort_values(by='mpg').tail(5))

print(mtcars[['car','mpg','cyl']][mtcars.cyl == 8].sort_values(by='mpg').head(3))

print("Srednja potrosnja automobila s 6 cilindara iznosi: ")
print(mtcars['mpg'][mtcars.cyl == 6].mean())

print("Srednja potrosnja automobila s 4 cilindra mase izmedu 2000 i 2200: ")
print(mtcars['mpg'][(mtcars.cyl == 4) & (mtcars.wt<=2.2) & (mtcars.wt>=2.0)].mean())

rucni = mtcars[mtcars.am == 1].shape[0]
automatski = mtcars[mtcars.am == 0].shape[0]
print("Automobila s rucnim mjenjacem ima " + str(rucni) + " a s automatskim ima " + str(automatski))

print("Automobila s automatskim mjenjacem i 100+ konjskih snaga ima: " + str(mtcars[(mtcars.am == 0) & (mtcars.hp > 100)].shape[0]))

mtcars['kg'] = mtcars.wt * 1000

print(mtcars[['car','kg']])