import time

class OrientationApp:
    def __init__(self, port="/dev/ttyUSB0", baudrate=115200, dt=0.05):
        self.reader = MagReader(port, baudrate)
        self.estimator = OrientationEstimator(dt)
        self.dt = dt