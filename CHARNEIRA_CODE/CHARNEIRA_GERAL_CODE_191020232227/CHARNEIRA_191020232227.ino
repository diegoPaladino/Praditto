#include <AccelStepper.h>

// Definições para o motor de passo
#define STEP_PIN_X 2
#define DIR_PIN_X 3

#define STEP_PIN_Z 4
#define DIR_PIN_Z 5

AccelStepper stepperX(AccelStepper::DRIVER, STEP_PIN_X, DIR_PIN_X);
AccelStepper stepperZ(AccelStepper::DRIVER, STEP_PIN_Z, DIR_PIN_Z);

void setup() {
  // Inicialização de código aqui (configuração de pinos, inicialização de LCD, etc.)
  stepperX.setMaxSpeed(1000);
  stepperX.setAcceleration(500);
  stepperZ.setMaxSpeed(1000);
  stepperZ.setAcceleration(500);
}

void loop() {
  // Código para ler botões, selecionar modelo, mover motores, etc.
}
