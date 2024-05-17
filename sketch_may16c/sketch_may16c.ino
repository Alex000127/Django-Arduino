int LedPin = 13;

void setup() {
  Serial.begin(9600);  // Inicia la comunicación serial a 9600 bps
  pinMode(LedPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // Lee el comando enviado por la computadora
    if (command == "LED_ON") {
      digitalWrite(LedPin, HIGH);
      Serial.println("LED encendido");
    } else if (command == "LED_OFF") {
      digitalWrite(LedPin, LOW);
      Serial.println("LED apagado");
    } else {
      Serial.println("Comando desconocido");
    }
  }
  delay(100);  // Pequeño retardo para evitar saturar el puerto serial
}
