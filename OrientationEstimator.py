#Solves the Kinematic Part
from RotationMath import RotationMath
import numpy as np

class OrientationEstimator:
    def __init__(self, dt=0.05, m0=np.array([25.0, 0.0, 45.0])):
        self.dt = dt
        self.R = np.eye(3)  # Initial orientation
        self.m0 = m0
        self.history = []

    def update(self, m_measured, omega):
        self.R = RotationMath.evolve_rotation(self.R, omega, self.dt)
        m_pred = RotationMath.predict_field(self.R, self.m0)
        error = np.linalg.norm(m_measured - m_pred)
        self.history.append((self.R.copy(), error))
        return self.R, error
    