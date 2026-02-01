import socket 
import RPi.GPIO as GPIO

send = "no"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2788))
s.listen(5)

def button_callback(channel):
    global send
    print(f"{send}")
    #clientsocket.send(bytes("STOP!", "utf-8"))
    #print("sending for true event")
    send = "yes"

GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback)

while True:
    clientsocket, address = s.accept()
    clientsocket.send(bytes(f"{send}", "utf-8"))
    if (send == "yes"):
        send = "no"

GPIO.cleanup()
