import pandas as pd

data = {
    "calories": [550, 450, 650],
    "duration": [4, 7, 2]
}

calories_duration_df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(calories_duration_df)
# print(calories_duration_df.loc[0])
# print(calories_duration_df.loc[[0,0]])

# print(calories_duration_df)
# print(calories_duration_df.loc["day2"])


