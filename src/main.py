import machine
import dht
import time

# Configurações de Hardware
pino_led = machine.Pin(2, machine.Pin.OUT)
pino_buzzer = machine.Pin(13, machine.Pin.OUT)
pino_botao = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
sensor = dht.DHT22(machine.Pin(15))

# Variáveis de Controle
TEMP_MIN = 2.0
TEMP_MAX = 8.0
estado = "NORMAL"
ultimo_print = 0

print("Teste: Sistema de Monitoramento de Vacinas PNAAT") # OBRIGATÓRIO PARA O CI/CD

while True:
    # Leitura não-bloqueante a cada 2 segundos
    agora = time.ticks_ms()
    if time.ticks_diff(agora, ultimo_print) >= 2000:
        ultimo_print = agora
        try:
            sensor.measure()
            t = sensor.temperature()
            print(f"Status: {estado} | Temp: {t}°C")
            
            if t < TEMP_MIN or t > TEMP_MAX:
                if estado != "SILENCIADO":
                    estado = "ALERTA"
            else:
                estado = "NORMAL"
                pino_led.off()
                pino_buzzer.off()
        except:
            print("Erro ao ler sensor DHT22")

    # Máquina de Estados
    if estado == "ALERTA":
        pino_led.value(not pino_led.value())
        pino_buzzer.value(not pino_buzzer.value())
        time.sleep(0.1)
        if pino_botao.value() == 0: # Se apertar o botão
            estado = "SILENCIADO"
            pino_buzzer.off()

    elif estado == "SILENCIADO":
        pino_led.value(not pino_led.value())
        time.sleep(0.5) # Pisca mais lento