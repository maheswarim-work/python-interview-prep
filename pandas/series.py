import pandas as pd

# a = [1, 7, 2]
#
# var1 = pd.Series(a)
# print(var1)
# print(var1[0])
#
# b = [2, 1, 4]
# var2  = pd.Series(b, index=['first', 'second', 'third'])
# print(var2)
# print(var2['third'])

calories = {"Monday": 550, "Tuesday": 700, "Wednesday": 600}

# cal = pd.Series(calories)
# print(cal)
# print(calories)

day_cal = pd.Series(calories, index=['Monday', 'Wednesday'])
print(day_cal)

