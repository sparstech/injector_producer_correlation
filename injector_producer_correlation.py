# I suspect water injection is affecting production in 15 wells.
# Write a program that computes correlation manually
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
# Sample data for water injection and production rates
data = {
    "water_injection": [100, 150, 200, 250, 300, 350, 400],
    "production_rate": [120, 180, 240, 300, 360, 420, 480]
}
df = pd.DataFrame(data)
# Calculate correlation manually
def manual_correlation(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y2 = sum(yi ** 2 for yi in y)
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = np.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))
    
    if denominator == 0:
        return 0
    return numerator / denominator
correlation = manual_correlation(df["water_injection"], df["production_rate"])
print(f"Manual Correlation: {correlation}")
# Verify with scipy
scipy_correlation, _ = pearsonr(df["water_injection"], df["production_rate"])
print(f"SciPy Correlation: {scipy_correlation}")
# Plotting the data
plt.scatter(df["water_injection"], df["production_rate"])
plt.title("Water Injection vs Production Rate")
plt.xlabel("Water Injection")
plt.ylabel("Production Rate")
plt.show()
# The correlation values from manual calculation and SciPy should match closely.
#end of file