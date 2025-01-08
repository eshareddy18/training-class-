import pandas as pd

screen_time = [2, 4, 6]
sleep_hours = [8, 5, 9]
stu_name = ["Esha", "Nani", "Vivek"]

dict1 = {
    "screen_time": screen_time,
    "sleep_hours": sleep_hours,
    "stu_name": stu_name
}

print(dict1)

df = pd.DataFrame(dict1)
print(df)
