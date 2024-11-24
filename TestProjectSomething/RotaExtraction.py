import uuid
from cryptography.fernet import Fernet
import json
import pandas as pd

pd.set_option('display.max_columns', None)


class dataNormalisation:
    def dataExtraction(self, rota):
        df = pd.read_csv(rota)
        df.columns = range(len(df.columns))
        df = df.dropna(how="all")
        df.reset_index(drop=True, inplace=True)
        df.to_csv("E:\\The Rota Scheduler\\Test.csv", index=False)

        string_to_find_in = "Line Chef"
        string_to_find_out = "kitchen assistant"

        line_chef_rows = df[df.iloc[:, 0] == string_to_find_in].index
        ka_rows = df[df.iloc[:, 0] == string_to_find_out].index

        start_row = line_chef_rows[0]
        end_row = ka_rows[0]
        selected_rows = df[start_row:end_row]
        selected_rows = selected_rows[selected_rows[1].notna()]
        selected_rows = selected_rows.drop(columns=[0, 2, 10])
        selected_rows.columns = range(len(selected_rows.columns))
        selected_rows.reset_index(drop=True, inplace=True)
        return selected_rows

    def hours_to_numeric(self, shift):
        if shift == 'OFF':
            return 0
        elif shift == 'Holiday':
            return -1
        else:
            # Example: Parse "0800-1700" to total hours worked (9 hours)
            start, end = shift.split(' - ')

            start_hours = int(start[:2])
            start_minutes = int(start[2:])
            end_hours = int(end[:2])
            end_minutes = int(end[2:])
            # print(start_hours, start_minutes, end_hours, end_minutes)

            # Calculate the total minutes worked
            total_minutes = (end_hours * 60 + end_minutes) - (start_hours * 60 + start_minutes)
            # print(total_minutes)
            # Calculate the hours and minutes from total minutes
            hours_worked = total_minutes // 60
            # print(hours_worked)
            minutes_worked = total_minutes % 60
            # print(minutes_worked)

            return f"{hours_worked:02d}:{minutes_worked:02d}"

    def nameEncryption(self, mapping_file_path, data, key_path):
        existing_mapping = {}
        key = Fernet.generate_key()
        with open(key_path, 'wb') as key_file:
            key_file.write(key)
        try:
            with open(mapping_file_path, "rb") as mapping_file:
                encrypted_data = mapping_file.read()
                decrypt_data = Fernet(key).decrypt(encrypted_data)
                existing_mapping = json.loads(decrypt_data.decode)
        except FileNotFoundError:
            pass

        names = data[0].tolist()

        for name in names:
            if name not in existing_mapping:
                unq_id = str(uuid.uuid4())
                existing_mapping[name] = unq_id

        encrypted_data = Fernet(key_path).encrypt(json.dumps(existing_mapping).encode())
        with open(mapping_file_path, "wb") as mapping_file:
            mapping_file.write(encrypted_data)



dataNormalisation = dataNormalisation()

selected_rows = dataNormalisation.dataExtraction("E:\The Rota Scheduler\ViewEmployeesOnRota.xls.csv")
day_columns = list(range(1, 8))
selected_rows[day_columns] = selected_rows[day_columns].applymap(lambda x: dataNormalisation.hours_to_numeric(x))
print(selected_rows)

# print(selected_rows.at[11, 2])

# shift_to_numeric("0830-1430")