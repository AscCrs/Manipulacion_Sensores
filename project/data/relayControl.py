import RPi.GPIO as GPIO

# Configuración de los pines GPIO para los canales de los relés
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
relay_pins = [17, 18, 27, 22]   # Reemplaza los números de los pines según corresponda
for pin in relay_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Función para cambiar el estado de los relés
def set_relay_state(relay_index, state):
    GPIO.output(relay_pins[relay_index], state)