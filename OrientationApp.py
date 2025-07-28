import time
import numpy as np
from OrientationEstimator import OrientationEstimator
from MagReader import MagReader

class OrientationApp:
    def __init__(self, port="COM4", baudrate=115200, dt=0.05):
        self.reader = MagReader(port, baudrate)
        self.estimator = OrientationEstimator(dt)
        self.dt = dt

    def run(self, steps=200):
        self.reader.start_stream()
        print("Reading data and estimating orientation...")

        for _ in range(steps):
            time.sleep(self.dt)
            latest = self.reader.get_latest()
            if not latest:
                continue
            m_measured = np.array(latest[-1])
            omega = np.array([0.01, 0.02, 0.01])  # Replace with real gyro data later
            R, error = self.estimator.update(m_measured, omega)
            print(f"Error: {error:.3f}, Orientation Matrix:\n{R}\n")

        self.reader.stop_stream()
