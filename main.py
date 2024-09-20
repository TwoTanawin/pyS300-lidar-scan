import serial
import time

class SickS300:
    def __init__(self, port='/dev/ttyUSB0', baudrate=500000):
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def open(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=1)
            time.sleep(2)  # Wait for the connection to stabilize
            print(f"Connected to Sick S300 on {self.port}")
        except serial.SerialException as e:
            print(f"Error opening serial port: {e}")

    def close(self):
        if self.serial:
            self.serial.close()
            print("Connection closed")

    def read_data(self):
        if self.serial:
            while True:
                if self.serial.in_waiting > 0:
                    raw_data = self.serial.read(self.serial.in_waiting)
                    self.process_data(raw_data)

    def process_data(self, data):
        print(f"Received (raw bytes): {data}")

if __name__ == "__main__":
    sick_s300 = SickS300(port='/dev/ttyUSB0')  # Update the port as necessary
    sick_s300.open()

    try:
        sick_s300.read_data()
    except KeyboardInterrupt:
        pass
    finally:
        sick_s300.close()
