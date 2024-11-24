import pandas as pd
from datetime import datetime, timedelta

# Sample shifts data (replace with your data)
shifts_data = {
    'Shift_Start': ['07:00', '08:30', '15:00', '15:00'],
    'Shift_End': ['15:00', '14:30', '23:00', '20:00']
}

# Create a DataFrame from the sample data
df = pd.DataFrame(shifts_data)


def calculate_proximity_score(row):
    # Define timeline points
    timeline_start = datetime.strptime('06:00', '%H:%M').time()
    timeline_mid = datetime.strptime('15:00', '%H:%M').time()
    timeline_end = datetime.strptime('23:30', '%H:%M').time()

    # Calculate shift midpoint
    shift_start = datetime.strptime(row['Shift_Start'], '%H:%M').time()
    shift_end = datetime.strptime(row['Shift_End'], '%H:%M').time()
    shift_midpoint = (datetime.combine(datetime.today(), shift_start) +
                      timedelta(minutes=(datetime.combine(datetime.today(), shift_end) -
                                         datetime.combine(datetime.today(), shift_start)).seconds / 2)).time()

    # Calculate proximity score based on shift midpoint and timeline points
    if shift_midpoint < timeline_mid:
        proximity_score = (shift_midpoint.hour * 60 + shift_midpoint.minute) / (timeline_mid.hour * 60 +
                                                                                timeline_mid.minute)
    else:
        proximity_score = 1 - ((shift_midpoint.hour * 60 + shift_midpoint.minute) - (timeline_mid.hour * 60 +
        timeline_mid.minute)) / ((timeline_end.hour * 60 + timeline_end.minute) -
                                 (timeline_mid.hour * 60 + timeline_mid.minute))

    return proximity_score


df['Proximity_Score'] = df.apply(calculate_proximity_score, axis=1)

# Display the DataFrame with the proximity scores
print(df)










# import pandas as pd
# import numpy as np
# from datetime import datetime, time
#
#
# shifts_data = {
#     "shift_start": ["7:30", "8:30", "15:00", "15:00"],
#     "shift_end": ["15:00", "14:30", "20:00", "23:00"]
# }
#
# df = pd.DataFrame(shifts_data)
#
# # Define the timeline start and end times
# timeline_start = datetime.combine(datetime.today(), time(7, 0))
# timeline_end = datetime.combine(datetime.today(), time(23, 30))
#
#
# # timeline_start = pd.to_datetime("7:00").time()
# # timeline_end = pd.to_datetime("23:30").time()
#
#
# def calculate_proximity_score(row):
#     shift_start = pd.to_datetime(row["shift_start"]).time()
#     shift_end = pd.to_datetime(row["shift_end"]).time()
#
#     projection_length = min(shift_end, timeline_end) - max(shift_start, timeline_start)
#
#     timeline_length = timeline_end-timeline_start
#
#     proximity_score = projection_length.total_seconds() / timeline_length.total_seconds()
#
#     return proximity_score
#
# df["Proximity_score"] = df.apply(calculate_proximity_score, axis=1)
#
# print(df)
#
#
