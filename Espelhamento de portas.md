#redes
# Espelhamento de portas

Um analisador de pacotes (também conhecido como sniffer de pacotes ou sniffer de tráfego) é normalmente um software que captura pacotes que entram e saem da placa de interface de rede (NIC). Nem sempre é possível ou desejável ter o analisador de pacotes no dispositivo que está sendo monitorado. Às vezes, é melhor em uma estação separada designada para capturar os pacotes.

Como os switches de rede podem isolar o tráfego, os sniffers de tráfego ou outros monitores de rede, como IDS, não podem acessar todo o tráfego em um segmento de rede. O espelhamento de portas é um recurso que permite que um switch faça cópias duplicadas do tráfego que passa por um switch e, em seguida, enviá-lo para fora uma porta com um monitor de rede conectado. O tráfego original é encaminhado da maneira usual. Um exemplo de espelhamento de porta é ilustrado na figura.

**Farejamento de tráfego usando um switch**

![[Pasted image 20240513112051.png]]










