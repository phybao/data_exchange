import serial
import time

# Detect and set the correct serial port
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)  # Allow time for the Arduino to reset

def send_data_to_arduino(data):
    """Send data to Arduino via USB serial."""
    if arduino.is_open:
        arduino.write(f"{data}\n".encode())  # Send data as bytes

def read_data_from_arduino():
    """Read data from Arduino via USB serial."""
    if arduino.in_waiting > 0:
        return arduino.readline().decode('utf-8').strip()  # Decode received bytes
    return None

try:
    while True:
        # Example: Send data to Arduino
        pi_data = "Hello from Pi"
        send_data_to_arduino(pi_data)
        print(f"Sent to Arduino: {pi_data}")
        
        # Example: Read data from Arduino
        arduino_data = read_data_from_arduino()
        if arduino_data:
            print(f"Received from Arduino: {arduino_data}")

        time.sleep(1)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Exiting program...")

finally:
    if arduino.is_open:
        arduino.close()
