
import bluetooth
import time
from evdev import InputDevice,list_devices, ecodes, categorize

arduino_mac = "BC:6A:D1:B8:29:3B"
port = 1

mandoPath = "/dev/input/event3"

dispositivos = bluetooth.discover_devices()
print("Dispositivos encontrados:", dispositivos)

devices = [InputDevice(path) for path in list_devices()]
for device in devices:
   print(device.path, device.name, device.phys)



## Inicia programa

gamepad = InputDevice("/dev/input/event3")

# Conectar al dispositivo Bluetooth

"""
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((arduino_mac, port))
print("Conectado al dispositivo receptor!")

try:
    for event in gamepad.read_loop():
        if event.type == ecodes.EV_KEY:
            # Mapear botones a comandos 
            if event.code == ecodes.BTN_A and event.value == 1:
                sock.send("F")  # Adelante
                print("Enviado: F")
            elif event.code == ecodes.BTN_B and event.value == 1:
                sock.send("B")  # Atrás
                print("Enviado: B")
except KeyboardInterrupt:
    sock.close()
    print("Conexión cerrada.")
"""


while True:
    for event in gamepad.read_loop():

        if event.type == ecodes.EV_KEY:
            # Mapear botones a comandos 

            #print(categorize(event))

            #Buttons
            if event.code == ecodes.BTN_A and event.value == 1:
                ##sock.send("B") 
                print("Enviado: B")
            if event.code == ecodes.BTN_B and event.value == 1:
                ##sock.send("A")
                print("Enviado: A")
            if event.code == ecodes.BTN_X and event.value == 1:
                ##sock.send("X")
                print("Enviado: X")
            if event.code == ecodes.BTN_Y and event.value == 1:
                ##sock.send("Y")
                print("Enviado: Y")

            #DPAD
            if event.code == ecodes.BTN_DPAD_DOWN and event.value == 1:
                ##sock.send("DPAD_DOWN")
                print("Enviado: DPAD_DOWN")
            if event.code == ecodes.BTN_DPAD_UP and event.value == 1:
                ##sock.send("DPAD_UP")
                print("Enviado: DPAD_UP")
            if event.code == ecodes.BTN_DPAD_LEFT and event.value == 1:
                ##sock.send("DPAD_LEFT")
                print("Enviado: DPAD_LEFT")
            if event.code == ecodes.BTN_DPAD_RIGHT and event.value == 1:
                ##sock.send("DPAD_RIGHT")
                print("Enviado: DPAD_RIGHT")
            
            #Trigger
            if event.code == ecodes.BTN_TL and event.value == 1:
                ##sock.send("BTN_TL")
                print("Enviado: BTN_TL")
            if event.code == ecodes.BTN_TL2 and event.value == 1:
                ##sock.send("BTN_TL2")
                print("Enviado: BTN_TL2")
            if event.code == ecodes.BTN_TR and event.value == 1:
                ##sock.send("BTN_RL")
                print("Enviado: BTN_RL")
            if event.code == ecodes.BTN_TR2 and event.value == 1:
                ##sock.send("BTN_TR2")
                print("Enviado: BTN_TR2") 
            

            #Thumb Buttons
            if event.code == ecodes.BTN_THUMBL and event.value == 1:
                ##sock.send("BTN_THUMBL")
                print("Enviado: BTN_THUMBL")
            if event.code == ecodes.BTN_THUMBR and event.value == 1:
                ##sock.send("BTN_THUMBR")
                print("Enviado: BTN_THUMBR")

