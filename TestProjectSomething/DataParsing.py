import os
import pandas as pd
from datetime import datetime

pd.set_option("display.max_columns", None)
filepath = "E:/The Rota Scheduler/ViewEmployeesOnRota.xls.csv"

start_text = "Line Chef"
end_text = "Kitchen assistant"

df = pd.read_csv(filepath, header=None)


start_index = df[df.apply(lambda row: row.astype(str).str.contains(start_text, case=False).any(), axis=1)].index[0]
end_index = df[df.apply(lambda row: row.astype(str).str.contains(end_text, case=False).any(), axis=1)].index[0]

extracted_df = df.iloc[start_index + 1:end_index]
new_df = extracted_df.dropna(how="all")

on_drop = "ON"
new_df = new_df[~new_df.apply(lambda row: row.astype(str).str.contains(on_drop).any(), axis=1)]
new_df = new_df.dropna(axis=1)
new_df.columns = range(len(new_df.columns))
new_df = new_df.reset_index(drop=True)
new_df = new_df.drop(columns=8, axis=1)
print(new_df)


def get_unique_filename(base_filename, directory):
    # Get today's date and format it as YYYYMMDD
    date_str = datetime.now().strftime('%Y%m%d')

    # Start with no suffix for the filename (i.e., try "rota.csv" first)
    i = 0
    while True:
        # If this is the first iteration, don't add a number to the filename
        if i == 0:
            filename = f"{date_str}_{base_filename}"
        else:
            # Split the base filename into name and extension
            name, extension = os.path.splitext(base_filename)
            # Add the number to the filename
            filename = f"{date_str}_{name}{i}{extension}"

        # Add the directory path to the filename
        full_path = os.path.join(directory, filename)

        # If a file with this name does not exist, return the filename
        if not os.path.isfile(full_path):
            return full_path

        # Otherwise, increment the number and try again
        i += 1


savefile_name = get_unique_filename("data.csv", "E:/The Rota Scheduler/")
new_df.to_csv(savefile_name, index=False)