import numpy as np
from scipy.optimize import minimize


# Function to minimize (penalizes outcomes outside the desired range)
def objective_function(weights, shifts, timeline_start, timeline_end):
    total_penalty = 0
    for shift in shifts:
        w1, w2, w3 = weights
        s, e, d = shift

        # Calculate midpoint of the shift as a fraction of the timeline's length
        midpoint_fraction = ((s + e) / 2) * (1 / (timeline_end - timeline_start))

        # Calculate the fraction of the shift's duration in the timeline
        fraction = d / (timeline_end - timeline_start)

        # Calculate desired t values range for the shift
        desired_t_start = midpoint_fraction - (fraction / 2)
        desired_t_end = midpoint_fraction + (fraction / 2)

        # Calculate calculated t using the given weights and parameters
        calculated_t = w1 * np.exp(-k * (timeline_end - e)) + w2 * np.exp(-k * (s - timeline_start)) + w3 * d

        # Penalize if calculated_t falls outside the desired range
        if calculated_t < desired_t_start:
            total_penalty += (desired_t_start - calculated_t) ** 2
        elif calculated_t > desired_t_end:
            total_penalty += (calculated_t - desired_t_end) ** 2

    return total_penalty


# Initial guess for weights and other parameters
initial_weights = np.array([1, 1, 1])  # Initial guess as a NumPy array
k = 0.1  # Rate of decay

# List of shifts (start, end, duration)
shifts = [(7, 15, 8), (8.5, 14.5, 6), (12, 20, 8), (15, 23, 8), (15, 23.5, 8.5)]  # Example shifts

# Constants for timeline start and end
TIMELINE_START = 0
TIMELINE_END = 24

# Optimization to find weights
result = minimize(objective_function, initial_weights, args=(shifts, TIMELINE_START, TIMELINE_END),
                  bounds=[(0, None)] * 3)  # Ensuring weights are non-negative

# Extracting optimized weights
optimized_weights = result.x

# Output optimized weights
print("Optimized Weights (w1, w2, w3):", optimized_weights)

def tau_func(s1, s2, d):
    t1 = 0
    t2 = 24
    s1 = s1
    s2 = s2
    d = d
    w1 = optimized_weights[0]
    w2 = optimized_weights[1]
    w3 = optimized_weights[2]

    calc_t = w1 * np.exp(-k * (t2 - s2)) + w2 * np.exp(-k * (s1 - t1)) + w3 * d
    return calc_t

print(tau_func(7, 15, 8))
print(tau_func(12, 20, 8))
print(tau_func(15, 23, 8))