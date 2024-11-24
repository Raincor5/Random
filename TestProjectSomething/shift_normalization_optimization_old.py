import numpy as np
from scipy.optimize import minimize


# Function to minimize (penalizes outcomes outside the desired range)
def objective_function(weights, shifts, desired_t_ranges):
    total_penalty = 0
    for shift, (min_desired_t, max_desired_t) in zip(shifts, desired_t_ranges):
        w1, w2, w3 = weights
        shift_start, shift_end, shift_duration = shift
        calculated_t = w1 * 2.71 ** (-k * (timeline_end - shift_end)) + w2 * 2.71 ** (
                    -k * (shift_start - timeline_start)) + w3 * shift_duration

        # Penalize if calculated_t falls outside the desired range
        if calculated_t < min_desired_t:
            total_penalty += (min_desired_t - calculated_t) ** 2
        elif calculated_t > max_desired_t:
            total_penalty += (calculated_t - max_desired_t) ** 2

    return total_penalty


# Initial guess for weights and other parameters
initial_weights = np.array([1, 1, 1])  # Initial guess as a NumPy array
k = 0.08  # Rate of decay
timeline_start, timeline_end = 0, 24  # Timeline start and end

# List of shifts (start, end)
shifts = [(7, 15, 8), (8.5, 14.5, 6), (12, 20, 8), (15, 23.5, 8.5)]  # Example shifts

# Desired outcomes range for each shift (min, max)
desired_t_ranges = [(0.2, 0.3), (0.10, 0.45), (0.5, 0.5), (0.5, 1)]

# Optimization to find weights
result = minimize(objective_function, initial_weights, args=(shifts, desired_t_ranges),
                  bounds=[(0, None)] * 3)  # Ensuring weights are non-negative

# Extracting optimized weights
optimized_weights = result.x

# Output optimized weights
print("Optimized Weights (w1, w2, w3):", optimized_weights)