import time
import RPi.GPIO as GPIO
from lcd import drivers
import math

# LCD configuration
lcd = drivers.Lcd()

# Pin definitions
SELECIONAMODELO_PIN = 26  # Pin where the voltage divider is connected
DIR_PIN_X = 5
STEP_PIN_X = 28
DIR_PIN_Y = 21
STEP_PIN_Y = 22

LEDPI_PIN = 25

LED_PIN = 10
SOLENOIDE_PIN = 18
LED_TEST_PIN = 10  # Pin for LED testing

MOTORVIBRA_PIN = 20

LEDCANCEL_PIN = 13

# Endstops and zero position X and Y
ENDSTOPX_BUTTON_XE_PIN = 17  # Right endstop
ENDSTOPX_BUTTON_XD_PIN = 28  # Left endstop
INICIOY_BUTTON_YT_PIN = 19  # Y top endstop
INICIOYB_BUTTON_YB_PIN = 16  # Y bottom endstop

# Button pins
SELECT_BUTTON_PIN = 2  # Button for selection
START_BUTTON_PIN = 3   # Button to start
STOP_BUTTON_PIN = 4    # Button to stop

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(LED_TEST_PIN, GPIO.OUT)

GPIO.setup(LEDPI_PIN, GPIO.OUT)

GPIO.setup(SOLENOIDE_PIN, GPIO.OUT)
GPIO.setup(MOTORVIBRA_PIN, GPIO.OUT)

GPIO.setup(LEDCANCEL_PIN, GPIO.OUT)

# Endstops
GPIO.setup(ENDSTOPX_BUTTON_XE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ENDSTOPX_BUTTON_XD_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INICIOY_BUTTON_YT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INICIOYB_BUTTON_YB_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Buttons
GPIO.setup(SELECT_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(START_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(STOP_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Motor pins
GPIO.setup(STEP_PIN_X, GPIO.OUT)
GPIO.setup(DIR_PIN_X, GPIO.OUT)
GPIO.setup(STEP_PIN_Y, GPIO.OUT)
GPIO.setup(DIR_PIN_Y, GPIO.OUT)
GPIO.output(STEP_PIN_X, GPIO.LOW)
GPIO.output(DIR_PIN_X, GPIO.LOW)
GPIO.output(STEP_PIN_Y, GPIO.LOW)
GPIO.output(DIR_PIN_Y, GPIO.LOW)

GPIO.output(LEDPI_PIN, GPIO.HIGH)

# Initialize LCD
lcd.lcd_display_string("Welcome!", 1)
lcd.lcd_display_string(">Praditto<", 2)
time.sleep(1)

# Global variables
stepsCountX = 0
stepsCountY = 0
movementStarted = False
setupCarregado = True
setupCarregadoInicio = True

state = 0
lastStepTime = 0
stepInterval = 100  # Step interval in milliseconds

# Movement structure
class Movement:
    def __init__(self, motor, steps, clockwise, label, millimeters):
        self.motor = motor
        self.steps = steps
        self.clockwise = clockwise
        self.label = label
        self.millimeters = millimeters

# Function declarations
def setupAlbert():
    pass

def loopAlbert():
    pass

def setupBill():
    pass

def loopBill():
    pass

def setupStart():
    pass

def loopStart():
    pass

currentLoop = None

def setup():
    lcd.lcd_clear()
    lcd.lcd_display_string(">by Praditto<", 3)
    lcd.lcd_display_string("Setup Initialized", 1)
    time.sleep(0.1)

    GPIO.output(SOLENOIDE_PIN, GPIO.LOW)
    GPIO.output(MOTORVIBRA_PIN, GPIO.LOW)

    print("Setup Initialized")

def selecionarModelo(valor, faixaMinima, faixaMaxima, estadoAnterior, nomeModelo, loopModelo):
    if faixaMinima <= valor <= faixaMaxima and valor != estadoAnterior:
        global currentLoop
        estadoAnterior = valor
        print("Selection:", nomeModelo)
        lcd.lcd_clear()
        lcd.lcd_display_string(">by Praditto<", 3)
        lcd.lcd_display_string("Selected Model:", 1)
        lcd.lcd_display_string(nomeModelo, 2)
        currentLoop = loopModelo

def loop():
    global setupCarregado, currentLoop, voltarSelecaoModelo, modeloAlbertSelecionado

    # Read analog value from the selection pin
    valorRecebido = GPIO.input(SELECIONAMODELO_PIN)
    voltage = valorRecebido * (3.3 / 1023.0)

    print("Raw value:", valorRecebido, ", Voltage:", voltage, "V")

    # Restore selection if the received value is zero and selection was not restored
    if valorRecebido == 8 and not voltarSelecaoModelo:
        lcd.lcd_clear()
        lcd.lcd_display_string(">by Praditto<", 3)
        lcd.lcd_display_string("Setup Loaded:", 1)
        lcd.lcd_display_string("CHOOSE A MODEL", 2)
        currentLoop = None
        voltarSelecaoModelo = True
        modeloAlbertSelecionado = False

    else:
        # Select the model based on the analog reading
        if not modeloAlbertSelecionado and valorRecebido == 1015:
            print("Selection: Albert")
            lcd.lcd_clear()
            lcd.lcd_display_string(">by Praditto<", 3)
            lcd.lcd_display_string("Selected Model:", 1)
            lcd.lcd_display_string("ALBERT", 2)
            currentLoop = loopAlbert
            modeloAlbertSelecionado = True

        selecionarModelo(valorRecebido, 200, 300, estadoAnteriorAlbert, "ALBERT", loopAlbert)
        selecionarModelo(valorRecebido, 1000, 1150, estadoAnteriorBill, "BILL", loopBill)

    if GPIO.input(SELECT_BUTTON_PIN) == GPIO.LOW:
        if currentLoop == loopStart or currentLoop == loopBill:
            print("Selection: Albert")
            lcd.lcd_clear()
            lcd.lcd_display_string(">by Praditto<", 3)
            lcd.lcd_display_string("Selected Model:", 1)
            lcd.lcd_display_string("ALBERT", 2)
            currentLoop = loopAlbert
            modeloAlbertSelecionado = True
        else:
            print("Selection: Bill")
            lcd.lcd_display_string(" BILL ", 2)
            currentLoop = loopBill

    if currentLoop is not None:
        currentLoop()

if __name__ == "__main__":
    setup()
    while True:
        loop()