👤 Identificação do Candidato
Nome completo: Heitor Lacerda Santana de Sousa

1️⃣ Visão Geral da Solução
O projeto consiste em um Sistema de Monitoramento para Cadeia de Frio, focado na preservação de vacinas e medicamentos termolábeis.

Objetivo: Garantir que a temperatura permaneça na faixa crítica de 2°C a 8°C.

Funcionamento: O sistema monitora a temperatura via sensor DHT22. Caso saia da faixa, aciona um alerta visual (LED) e sonoro (Buzzer).

Interação: O usuário pode silenciar o alarme sonoro pressionando um botão (Acknowledge), mas o alerta visual permanece até que a temperatura seja normalizada.

2️⃣ Arquitetura do Sistema Embarcado
A arquitetura foi desenhada para ser robusta e não-bloqueante:

Fluxo Principal: O código utiliza time.ticks_ms() para realizar leituras a cada 2 segundos sem travar a execução do processador (evitando o uso de time.sleep no loop principal).

Máquina de Estados: O firmware alterna entre os estados NORMAL, ALERTA e SILENCIADO.

Interação de Componentes: O sensor DHT22 fornece os dados de entrada; o ESP32 processa a lógica de estados e comanda as saídas (LED e Buzzer). O botão atua como uma interrupção de controle de estado.

3️⃣ Componentes Utilizados na Simulação
Placa: ESP32 DevKit V4.

Sensor DHT22: Monitoramento de temperatura e umidade com alta precisão.

LED Vermelho: Indicador visual de estado crítico ou atenção.

Buzzer (Piezo): Alerta sonoro para emergências térmicas.

Pushbutton: Botão de interação para confirmação e silenciamento de alertas.

4️⃣ Decisões Técnicas Relevantes
Lógica Não-Bloqueante: Essencial para garantir que o sistema responda a eventos (como o clique do botão) instantaneamente, mesmo durante o intervalo entre leituras do sensor. 

Máquina de Estados: Facilita a manutenção do código e garante que o comportamento do sistema seja previsível e organizado.

Palavra-Chave de Validação: Inclusão do print "Teste:" no início do código para garantir a compatibilidade com o pipeline de CI/CD do GitHub Actions.

5️⃣ Resultados Obtidos
Simulação Funcional: O sistema identifica variações de temperatura no Wokwi e altera os estados corretamente.

Requisitos Atendidos: Lógica robusta, diagrama organizado e execução bem-sucedida nas GitHub Actions.

Interface de Usuário: O sistema de "Acknowledge" via botão funciona perfeitamente, permitindo a gestão do alarme sonoro de forma independente do visual.

6️⃣ Comentários Adicionais
Aprendizado: O maior desafio foi integrar a lógica de MicroPython com o fluxo de build via Docker presente no repositório, garantindo que o sistema de arquivos fs.bin fosse gerado corretamente.

Melhorias: Em um cenário real, adicionaria o protocolo MQTT para enviar esses dados para um dashboard em nuvem (ex: ThingsBoard ou Azure IoT).