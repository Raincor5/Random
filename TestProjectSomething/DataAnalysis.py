import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import re
import multiprocessing as mp


def get_most_recent_rota(directory):
    # List all files in the specified directory
    files = os.listdir(directory)

    # Define a regular expression pattern to match filenames in the format "YYYYMMDD_rotaNUMBER.csv"
    pattern = r'(\d{8})_rota(\d+)\.csv'

    # Initialize variables to track the most recent date, number, and filename
    most_recent_date = 00000000
    most_recent_number = -1
    most_recent_rota_file_name = ""

    for rota_file in files:
        match = re.match(pattern, rota_file)
        if match:
            date_part, number_part = match.groups()
            date_part = int(date_part)
            number_part = int(number_part)

            # Compare both date and number to find the most recent file
            if date_part > int(most_recent_date) or (date_part == int(most_recent_date) and number_part >
                                                     int(most_recent_number)):
                most_recent_date = date_part
                most_recent_number = number_part
                most_recent_rota_file_name = rota_file

    if most_recent_rota_file_name:
        return most_recent_rota_file_name
    else:
        print("No valid date and number found in the matching CSV files.")
        return None


df = pd.read_csv("E:/The Rota Scheduler/" + get_most_recent_rota("E:/The Rota Scheduler"), index_col=0)

print(df)


def showheatma():
    plt.figure(figsize=(8, 6))

    heatmap = plt.imshow(df, cmap="coolwarm", interpolation="nearest")
    plt.colorbar(heatmap)


    plt.xticks(range(len(df.columns)), df.columns)
    plt.yticks(range(len(df.index)), df.index)
    plt.xlabel('Columns')
    plt.ylabel('Rows')
    plt.title('Heatmap of DataFrame with Row Indices')


def showEmployeeNumberByDay():
    morn = "1"
    night = "2"

    counts_1 = {}
    counts_2 = {}

    for col in df.columns:
        col_str = df[col].astype(str)  # Convert the column to string
        counts_1[col] = col_str.str.count(morn).sum()
        counts_2[col] = col_str.str.count(night).sum()

    plt.figure(figsize=(8, 6))
    x_labels = df.columns
    x_positions = range(len(x_labels))

    plt.bar(x_positions, list(counts_1.values()), width=0.4, label=f'Count of "{morn}"')
    plt.bar([x + 0.4 for x in x_positions], list(counts_2.values()), width=0.4, label=f'Count of "{night}"')

    # Set X-axis labels and rotate them for readability
    plt.xticks(x_positions, x_labels, rotation=90)

    # Add labels and a legend
    plt.xlabel('Columns')
    plt.ylabel('Count')
    plt.title('Count of shift types by day')
    plt.legend()

    # Show the bar chart
    plt.tight_layout()


def showEmployeeOffNumberByDay():
    off = "3"
    counts = {}

    for col in df.columns:
        col_str = df[col].astype(str)
        counts[col] = col_str.str.count(off).sum()

    plt.figure(figsize=(8, 6))
    x_labels = df.columns
    x_position = range(len(x_labels))

    plt.bar(x_position, list(counts.values()), width=0.5, label=f'Count of "{off}"')

    plt.xticks(x_position, x_labels, rotation=90)

    plt.xlabel("Day number")
    plt.ylabel("Count of employees off")
    plt.title("Count of employees off by day")

    plt.tight_layout()


if __name__ == "__main__":
    with mp.Pool(processes=3) as pool:
        # Use the pool to execute the functions concurrently
        pool.map(showheatma(), [])
        pool.map(showEmployeeNumberByDay(), [])
        pool.map(showEmployeeOffNumberByDay(), [])

        plt.show()


