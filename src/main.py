import machine
import dht
import time

# OBRIGATÓRIO: O robô do GitHub Actions espera ler esta palavra
print("Teste") 

# Configurações de Hardware
sensor = dht.DHT22(machine.Pin(15))
led = machine.Pin(2, machine.Pin.OUT)
buzzer = machine.Pin(13, machine.Pin.OUT)
botao = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)

estado = "NORMAL"
ultimo_tempo = 0

while True:
    agora = time.ticks_ms()
    
    # Leitura a cada 2 segundos (não-bloqueante)
    if time.ticks_diff(agora, ultimo_tempo) >= 2000:
        ultimo_tempo = agora
        try:
            sensor.measure()
            temp = sensor.temperature()
            print(f"Temp: {temp}C | Estado: {estado}")
            
            if temp < 2 or temp > 8:
                if estado != "SILENCIADO":
                    estado = "ALERTA"
            else:
                estado = "NORMAL"
                led.off()
                buzzer.off()
        except:
            pass

    # Máquina de Estados
    if estado == "ALERTA":
        led.value(not led.value())
        buzzer.value(not buzzer.value())
        time.sleep(0.1)
        if botao.value() == 0:
            estado = "SILENCIADO"
            buzzer.off()
            
    elif estado == "SILENCIADO":
        led.value(not led.value())
        time.sleep(0.5)