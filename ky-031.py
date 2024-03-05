# import Pin, ADC y PWM
from machine import Pin, SoftI2C
from time import sleep

# Definimos pines del sensor de choque
shock_sensor = Pin(34, Pin.IN)
led = Pin(2, Pin.OUT)

# Obtenemos el modulo para el display
import ssd1306

# Declaramos un objeto con los pines utilizados para la interfaz i2c
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Limpiamos el display
    display.fill(0)
    
    # Leemos el estado del sensor de choque
    shock_state = shock_sensor.value()
    
    # Escribimos el estado del sensor en el display
    if shock_state == 1:
        display.text('Choque Detectado', 0, 0, 1)
        led.off()  # Apaga el LED
    else:
        display.text('Sin Choque', 0, 0, 1)
        led.on()   # Enciende el LED
    
    # Actualizamos el display
    display.show()
    
    # Esperamos un poco para evitar lecturas demasiado rápidas
    sleep(1)

