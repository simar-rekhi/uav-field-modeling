#this contains the math functions on SO(3)

import numpy as np
from scipy.linalg import expm

class RotationMath:
    @staticmethod
    def skew(omega):
        return np.array([
            [0, -omega[2], omega[1]],
            [omega[2], 0, -omega[0]],
            [-omega[1], omega[0], 0]
        ])
    
    @staticmethod
    def evolve_rotation(R, omega, dt):
        Omega = RotationMath.skew(omega)
        return R @ expm(Omega *dt)
    
    @staticmethod
    def predict_field(R, m0):
        return R.T @ m0