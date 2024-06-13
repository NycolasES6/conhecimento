#redes 
# Segmentos de rede local e remota

Dentro de uma LAN, é possível colocar todos os hosts em uma única rede local ou dividi-los entre várias redes conectadas por um dispositivo na camada de distribuição. A forma como esse posicionamento é determinado depende dos resultados desejados.

## Todos os hosts em um segmento de rede local

Colocar todos os hosts em uma única rede local permite que eles sejam vistos por todos os outros hosts. Isso ocorre porque existe um domínio da broadcast e os hosts usam o ARP para se localizarem.

Em um projeto de rede simples, pode ser vantajoso manter todos os hosts em uma única rede local. Entretanto, à medida que as redes crescem, o aumento de tráfego diminui a velocidade e o desempenho da rede. Nesse caso, pode valer a pena mover alguns hosts para uma rede remota.

Vantagens de um único segmento local:

- Adequado para redes mais simples
- Menos complexidade e menor custo de rede
- Permite que os dispositivos sejam “vistos” por outros dispositivos
- Transferência de dados mais rápida - comunicação mais direta
- Facilidade de acesso ao dispositivo

Desvantagens de um único segmento local:

- Todos os hosts estão em um domínio de broadcast que causa mais tráfego no segmento e pode retardar o desempenho da rede
- Mais difícil de implementar QoS
- Mais difícil de implementar segurança

## Hosts em um segmento remoto

Colocando hosts adicionais em uma rede remota diminuirá o impacto em demandas de tráfego. No entanto, os hosts em uma rede não poderão se comunicar com hosts na outra rede sem o uso de roteamento. Os roteadores aumentam a complexidade da configuração de rede e podem introduzir latência (ou seja, atraso) nos pacotes enviados de uma rede local para outra.

Vantagens:

- Mais adequado para redes maiores e mais complexas
- Divide domínios de transmissão e reduz o tráfego
- Pode melhorar o desempenho em cada segmento
- Deixa as máquinas invisíveis para as pessoas em outros segmentos de rede local
- Pode fornecer segurança avançada
- Pode melhorar a organização de rede

Desvantagens:

- Exige o uso de roteamento (camada de distribuição)
- O roteador pode retardar o tráfego entre segmentos
- Mais complexidade e custos (exige roteador)










