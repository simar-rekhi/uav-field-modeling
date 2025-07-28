import pandas as pd
import numpy as np
from OrientationEstimator import OrientationEstimator

# --- Step 1: Load CSV data ---
df = pd.read_csv("raw.csv")

# Ensure columns exist
if not {'x', 'y', 'z'}.issubset(df.columns):
    raise ValueError("CSV must contain 'x', 'y', and 'z' columns")

# Convert to numpy array (N, 3)
mag_data = df[['x', 'y', 'z']].to_numpy(dtype=float)

# --- Step 2: Initialize Estimator ---
dt = 0.05  # time step in seconds
estimator = OrientationEstimator(dt)
omega = np.array([0.01, -0.02, 0.015])  # Simulated angular velocity

# --- Step 3: Run Orientation Simulation ---
for i, m in enumerate(mag_data):
    R, err = estimator.update(m, omega)
    print(f"[{i}] Magnetometer: {m}, Error: {err:.3f}\nOrientation:\n{R}\n")