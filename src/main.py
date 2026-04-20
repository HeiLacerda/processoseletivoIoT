import machine
import dht
import time

# O robô do CI ainda vai tentar ler isso
print("Teste") 

# Configuração dos Pinos
sensor = dht.DHT22(machine.Pin(15))
led_azul = machine.Pin(2, machine.Pin.OUT)   # Temperatura OK
led_vermelho = machine.Pin(4, machine.Pin.OUT) # Alerta
buzzer = machine.Pin(5, machine.Pin.OUT)
botao_ack = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

# Variáveis de Controle
alarme_silenciado = False
ultima_leitura = 0

print("Sistema de Monitoramento de Vacinas Iniciado...")

while True:
    agora = time.ticks_ms()
    
    # Leitura a cada 2 segundos (não bloqueante)
    if time.ticks_diff(agora, ultima_leitura) > 2000:
        try:
            sensor.measure()
            temp = sensor.temperature()
            print("Temp: {}°C".format(temp))
            
            # Lógica de Alerta (Faixa ideal: 2°C a 8°C)
            if temp < 2 or temp > 8:
                led_azul.off()
                led_vermelho.on()
                if not alarme_silenciado:
                    buzzer.on()
            else:
                led_azul.on()
                led_vermelho.off()
                buzzer.off()
                alarme_silenciado = False # Reseta o silenciador se a temp voltar ao normal
                
            ultima_leitura = agora
        except OSError as e:
            print("Erro na leitura do sensor.")

    # Lógica do Botão Acknowledge (Silenciar)
    if botao_ack.value() == 0:
        alarme_silenciado = True
        buzzer.off()
        print("Alarme silenciado pelo usuário.")
        time.sleep(0.2) # Debounce simples