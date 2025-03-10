import bluetooth
import time
from evdev import InputDevice, ecodes

# Configuración del servidor Bluetooth
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", 1))
server_sock.listen(1)

uuid = "00001101-0000-1000-8000-00805f9b34fb"

time.sleep(4)  # <-- Retraso crucial

# Anunciar servicio SPP
bluetooth.advertise_service(
    server_sock,
    "OrangePiServer",
    service_id=uuid,
    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
    profiles=[bluetooth.SERIAL_PORT_PROFILE],
    provider="Orange Pi",  # Nombre del proveedor
    description="Control de robot",  
    # Deshabilita perfiles de audio
    protocols=[bluetooth.RFCOMM]
)

print("Esperando conexión...")
client_sock, client_info = server_sock.accept()
print(f"Conectado a {client_info}")

# Configuración del mando

gamepad = InputDevice("/dev/input/event3")

# Conectar al dispositivo Bluetooth

try:
    while True:
        for event in gamepad.read_loop():

            if event.type == ecodes.EV_KEY:
                # Mapear botones a comandos 

                #print(categorize(event))

                #Buttons
                if event.code == ecodes.BTN_A and event.value == 1:
                    client_sock.send("B") 
                    print("Enviado: B")
                if event.code == ecodes.BTN_B and event.value == 1:
                    client_sock.send("A")
                    print("Enviado: A")
                if event.code == ecodes.BTN_X and event.value == 1:
                    client_sock.send("X")
                    print("Enviado: X")
                if event.code == ecodes.BTN_Y and event.value == 1:
                    client_sock.send("Y")
                    print("Enviado: Y")

                #DPAD
                if event.code == ecodes.BTN_DPAD_DOWN and event.value == 1:
                    client_sock.send("DPAD_DOWN")
                    print("Enviado: DPAD_DOWN")
                if event.code == ecodes.BTN_DPAD_UP and event.value == 1:
                    client_sock.send("DPAD_UP")
                    print("Enviado: DPAD_UP")
                if event.code == ecodes.BTN_DPAD_LEFT and event.value == 1:
                    client_sock.send("DPAD_LEFT")
                    print("Enviado: DPAD_LEFT")
                if event.code == ecodes.BTN_DPAD_RIGHT and event.value == 1:
                    client_sock.send("DPAD_RIGHT")
                    print("Enviado: DPAD_RIGHT")
                
                #Trigger
                if event.code == ecodes.BTN_TL and event.value == 1:
                    client_sock.send("BTN_TL")
                    print("Enviado: BTN_TL")
                if event.code == ecodes.BTN_TL2 and event.value == 1:
                    client_sock.send("BTN_TL2")
                    print("Enviado: BTN_TL2")
                if event.code == ecodes.BTN_TR and event.value == 1:
                    client_sock.send("BTN_RL")
                    print("Enviado: BTN_RL")
                if event.code == ecodes.BTN_TR2 and event.value == 1:
                    client_sock.send("BTN_TR2")
                    print("Enviado: BTN_TR2") 
                

                #Thumb Buttons
                if event.code == ecodes.BTN_THUMBL and event.value == 1:
                    client_sock.send("BTN_THUMBL")
                    print("Enviado: BTN_THUMBL")
                if event.code == ecodes.BTN_THUMBR and event.value == 1:
                    client_sock.send("BTN_THUMBR")
                    print("Enviado: BTN_THUMBR")
except KeyboardInterrupt:
    client_sock.close()
    server_sock.close()
