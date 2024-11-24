import uuid
from cryptography.fernet import Fernet
import json
import pandas as pd
import math

pd.set_option('display.max_columns', None)


class DataNormalization:
    def __init__(self, rota_file, mapping_file_path, key_path):
        self.rota_file = rota_file
        self.mapping_file_path = mapping_file_path
        self.key_path = key_path
        self.mapping = {}

    def execute_normalization(self):
        # Step 1: Data Extraction
        selected_rows = self.data_extraction()

        # Step 2: Hours to Numeric
        selected_rows = self.normalize_shifts(selected_rows)

        # Step 3: Name Encryption
        self.name_encryption(selected_rows)

        self.change_names(selected_rows)

        # Save the overall normalized rota
        normalized_file_path = "E:\\The Rota Scheduler\\NormalizedRota.csv"
        selected_rows.to_csv(normalized_file_path, index=False)
        print(f"Normalized Rota saved to {normalized_file_path}")

    def data_extraction(self):
        df = pd.read_csv(self.rota_file)
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

    def normalize_shifts(self, data):
        data.iloc[:, 1:] = data.iloc[:, 1:].applymap(self.shift_to_normalized_value)
        return data

    def shift_to_normalized_value(self, shift):
        if shift == 'OFF':
            return 0
        elif shift == 'Holiday':
            return -1
        else:
            return self.calculate_normalized_value(shift)

    def calculate_normalized_value(self, shift, D=24):
        # Similar logic as shift_to_numeric, calculate midpoint, start, and end times in hours
        start, end = shift.split('-')
        start_hours = int(start[:2]) + int(start[2:]) / 60
        end_hours = int(end[:2]) + int(end[2:]) / 60
        midpoint_hours = (start_hours + end_hours) / 2

        # Calculate the normalized value using the formula
        V = (math.e / D) * abs(
            1 - (math.e ** (midpoint_hours / D) + math.e ** (start_hours / D) + math.e ** (end_hours / D)))
        return V

    def load_key(self):
        try:
            with open(self.key_path, 'rb') as key_file:
                return key_file.read()
        except FileNotFoundError:
            # If key file doesn't exist, generate and save a new key
            key = Fernet.generate_key()
            with open(self.key_path, 'wb') as key_file:
                key_file.write(key)
            return key

    def name_encryption(self, data):
        existing_mapping = {}

        # Load the key
        key = self.load_key()

        try:
            # Load the existing mapping if it exists
            with open(self.mapping_file_path, "rb") as mapping_file:
                encrypted_data = mapping_file.read()
                decrypt_data = Fernet(key).decrypt(encrypted_data)
                existing_mapping = json.loads(decrypt_data.decode())
        except FileNotFoundError:
            pass

        names = data[0].tolist()

        for name in names:
            if name not in existing_mapping:
                unq_id = str(uuid.uuid4())
                existing_mapping[name] = unq_id

        # Encrypt the mapping data and save it
        with open(self.mapping_file_path, "wb") as mapping_file:
            encrypted_data = Fernet(key).encrypt(json.dumps(existing_mapping).encode())
            mapping_file.write(encrypted_data)

        # Store the mapping for later use
        self.mapping = existing_mapping

    def change_names(self, data):
        # Replace names with UUIDs using the mapping
        data[0] = data[0].map(self.mapping)


rota_file = "E:\\The Rota Scheduler\\ViewEmployeesOnRota.xls.csv"
mapping_file_path = "E:\\The Rota Scheduler\\name_mapping.enc"
key_path = "E:\\The Rota Scheduler\\encryption_key.key"

data_normalization = DataNormalization(rota_file, mapping_file_path, key_path)
data_normalization.execute_normalization()

