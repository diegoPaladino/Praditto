#define EMERGENCY_BUTTON_PIN 2  // Pin connected to the emergency stop button

void setup() {
  pinMode(EMERGENCY_BUTTON_PIN, INPUT);  // Set the emergency button pin as input
  // Inicialize outros componentes aqui, se necessário
}

void loop() {
  if (digitalRead(EMERGENCY_BUTTON_PIN) == HIGH) {
    // Código para lidar com a emergência
    emergencyStop();
  }
  // Outras funções do seu código aqui
}

void emergencyStop() {
  // Coloque aqui o código para desligar motores, sistemas, etc.
  // Por exemplo: digitalWrite(MOTOR_PIN, LOW);
}
