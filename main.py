from OrientationApp import OrientationApp

if __name__ == "__main__":
    app = OrientationApp(port="COM4", baudrate=115200, dt=0.05)
    app.run(steps=300)