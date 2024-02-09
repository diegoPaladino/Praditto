#include <Arduino.h>

// Definição dos pinos para as chaves fim de curso e botão de emergência
const int endstopPins[] = {2, 3, 4, 5}; // Substitua pelos pinos reais
const int emergencyButtonPin = 6; // Substitua pelo pino real

// Variável para controlar o estado do programa
volatile bool paused = false;

void setup() {
  // Inicia a comunicação serial
  Serial.begin(9600);
  
  // Configura os pinos como entrada
  for (int i = 0; i < 4; i++) {
    pinMode(endstopPins[i], INPUT);
  }
  pinMode(emergencyButtonPin, INPUT);
  
  // Ativa interrupções externas
  attachInterrupt(digitalPinToInterrupt(emergencyButtonPin), emergencyStop, FALLING);
  for (int i = 0; i < 4; i++) {
    attachInterrupt(digitalPinToInterrupt(endstopPins[i]), emergencyStop, FALLING);
  }
}

void loop() {
  // Seu código principal aqui
  
  // Verifica se o programa está pausado
  if (paused) {
    waitForCommand();
  }
  
  // Restante do seu código
}

void emergencyStop() {
  // Função chamada quando qualquer botão é pressionado
  paused = true;
}

void waitForCommand() {
  // Espera pelo comando de continuação ou reinício
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'A') {
      // Continua a execução
      paused = false;
    } else if (command == 'B') {
      // Reinicia o Arduino
      asm volatile ("  jmp 0");
    }
  }
}
