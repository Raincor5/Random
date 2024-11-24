import math

def calculate_normalized_value(midpoint, start, end, d):
    relative_position = math.exp(midpoint / d)
    relative_position_start = math.exp(start / d)
    relative_position_end = math.exp(end / d)
    normalized_value = abs((1 - (relative_position + relative_position_start + relative_position_end))
                           * (math.exp(1) / d))
    return normalized_value

def normalize_shift(shift_start, shift_end):
    d = 24
    midpoint = (shift_start + shift_end) / 2
    normalized_value = calculate_normalized_value(midpoint, shift_start, shift_end, d)
    return normalized_value

# List of shifts (start and end times)
shifts = [(4, 10), (15, 23), (8.5, 14.5), (12, 20), (15, 20), (18, 23.5)]

# Normalize each shift and store the results in a list
normalized_values = [normalize_shift(start, end) for start, end in shifts]

# Print normalized values for each shift
for idx, value in enumerate(normalized_values, start=1):
    print(f"Normalized Value for Shift {idx}: {value}")