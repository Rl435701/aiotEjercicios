# import Pin, ADC y PWM
from machine import Pin, ADC, SoftI2C
from time import sleep

# Definimos pines de joystick
sw = ADC(Pin(34))
vrx = ADC(Pin(33))
vry = ADC(Pin(35))

# Obtenemos el modulo para el display
import ssd1306

# Declaramos un objeto con los pines utilizados para la interfaz i2c
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Atenuacion
vrx.atten(ADC.ATTN_11DB)
vry.atten(ADC.ATTN_11DB)

# Resolucion a 4096 valores
vrx.width(ADC.WIDTH_12BIT)
vry.width(ADC.WIDTH_12BIT)

while True
    valorx = vrx.read()
    valory = vry.read()
    
    # Limpiamos el display
    display.fill(0)
    
    # Escribimos los valores del joystick en el display
    display.text('X {}'.format(valorx), 0, 0, 1)
    display.text('Y {}'.format(valory), 0, 10, 1)
    
    # Leemos el botón del joystick
    valorsw = sw.read()
    
    # Escribimos el estado del botón en el display
    if valorsw  0
        display.text('Boton No Presionado', 0, 20, 1)
    else
        display.text('Boton Presionado', 0, 20, 1)
    
    # Actualizamos el display
    display.show()
    
    # Esperamos un poco para evitar lecturas demasiado rápidas
    sleep(0.1)
