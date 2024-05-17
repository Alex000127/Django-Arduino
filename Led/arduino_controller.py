import serial

class ArduinoController:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.serial_connection = None
        self.connect()

    def connect(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate)
            print(f"Conexión serial abierta en {self.port}")
        except serial.SerialException as e:
            self.serial_connection = None
            print(f"No se pudo abrir el puerto serial: {e}")

    def send_command(self, command):
        if self.serial_connection is None:
            return "Error: No se pudo abrir el puerto serial."

        try:
            self.serial_connection.write((command + '\n').encode())
            response = self.serial_connection.readline().decode().strip()
            return response
        except Exception as e:
            return f"Error en la comunicación serial: {e}"

    def close(self):
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()
            print("Conexión serial cerrada.")
