import pygame
import time

# Inicializar pygame
pygame.init()

# Configurar el mando
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)  # Usar el primer mando conectado
joystick.init()

print(f"Mando conectado: {joystick.get_name()}")

try:
    while True:
        pygame.event.pump()  # Procesar eventos

        # Leer botones
        for i in range(joystick.get_numbuttons()):
            if joystick.get_button(i):
                print(f"Botón {i} presionado")

        """
            
        # Leer ejes (joysticks y gatillos)
        for i in range(joystick.get_numaxes()):
            axis_value = joystick.get_axis(i)
            if abs(axis_value) > 0.1:  # Ignorar valores cercanos a 0
                print(f"Eje {i}: {axis_value}")
        """
        # Leer hat (D-Pad)
        for i in range(joystick.get_numhats()):
            hat_value = joystick.get_hat(i)
            if hat_value != (0, 0):  # Ignorar valores neutros
                print(f"Hat {i}: {hat_value}")

        time.sleep(0.08)  # Evitar sobrecarga de la CPU

except KeyboardInterrupt:
    print("Programa terminado")