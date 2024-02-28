from machine import Pin
import time

# Cria um objeto Pin para controlar o LED embutido
led = Pin(25, Pin.OUT)

# Função para piscar o LED 4 vezes por segundo
def blink():
    for _ in range(4):
        led.toggle() # Alterna o estado do LED
        time.sleep(0.125) # Espera 125ms

while True:
    blink() # Chama a função blink
    time.sleep(0.5) # Espera 500ms entre cada série de piscadas
