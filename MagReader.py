import serial
import threading
from collections import deque

class MagReader:
    def __init__(self, port="COM4", baudrate=115200, maxlen=1000):
        self.port = port
        self.ser = serial.Serial(port, baudrate)
        self.data = deque(maxlen=maxlen)
        self.running = False

    def parse_line(self, line):
        try:
            values = list(map(float, line.strip().split(',')))
            return tuple(values) if len(values) == 3 else None
        except ValueError:
            return None

    def _read_loop(self):
        while self.running:
            line = self.ser.readline().decode('utf-8')
            point = self.parse_line(line)
            if point:
                self.data.append(point)

    def start_stream(self):
        self.running = True
        self.thread = threading.Thread(target=self._read_loop)
        self.thread.start()

    def stop_stream(self):
        self.running = False
        self.thread.join()

    def get_latest(self, n=1):
        return list(self.data)[-n:]
