import sys
import time

# O MicroPython as vezes demora a iniciar a serial, 
# então esperamos 1 segundo e depois imprimimos em loop.
time.sleep(1)
while True:
    print("Teste")
    time.sleep(2)