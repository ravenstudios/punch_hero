import serial
import time


class Sensors:
    def __init__(self):
        self.PORT = "/dev/ttyUSB0"
        self.BAUD = 115200
        self.error = False
        try:
            self.ser = serial.Serial(
                self.PORT,
                self.BAUD,
                timeout=0,      # non-blocking
                dsrdtr=False,
                rtscts=False
            )
        

            self.ser.setDTR(False)
            self.ser.setRTS(False)

            time.sleep(2)
            self.ser.reset_input_buffer()

        except (serial.SerialException, FileNotFoundError):
            print("⚠️ Sensor not connected")
            self.error = True

        print(f"Connected to {self.PORT} @ {self.BAUD}")

        self.left_hit = 0
        self.right_hit = 0
        self.buffer = b""

    def read_sensors(self):
        if not self.ser or not self.ser.is_open:
            return [self.left_hit, self.right_hit]

        n = self.ser.in_waiting
        if not n:
            return [self.left_hit, self.right_hit]

        chunk = self.ser.read(n)
        if not chunk:
            return [self.left_hit, self.right_hit]

        self.buffer += chunk

        while b"\n" in self.buffer:
            line, self.buffer = self.buffer.split(b"\n", 1)
            line = line.decode("utf-8", errors="ignore").strip()

            try:
                left, right = map(int, line.split(","))
                self.left_hit = left
                self.right_hit = right
            except ValueError:
                pass
        # print([self.left_hit, self.right_hit])
        return [self.left_hit, self.right_hit]
    


    def read_hit(self):
        if not self.ser or not self.ser.is_open:
            return None

        line = self.ser.readline().decode("utf-8", errors="ignore").strip()
        if not line:
            return None

        try:
            side, strength = line.split(",")
            return side, int(strength)
        except ValueError:
            return None


    def close(self):
        if self.ser and self.ser.is_open:
            self.ser.close()