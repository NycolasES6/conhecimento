#redes #CISCO #questionario
# Conceitos básicos de rede CISCO - 13_questionário sobre O Processo ARP

#### 1 - Qual é uma função do protocolo ARP?

- resolver um endereço IPv4 para um endereço MAC

#### 2 - Qual endereço de destino é usado em um quadro de solicitação ARP?

- FFFF.FFFF.FFFF

#### 3 - Qual afirmativa descreve o tratamento das requisições ARP no link local?

- Elas são recebidas e processadas por todos os dispositivos na rede local.

#### 4 - Que informações importantes são examinadas no cabeçalho do quadro Ethernet por um dispositivo de camada 2 para encaminhar os dados?

- endereço MAC destino

#### 5 - Quais são as duas funções dos endereços MAC em uma LAN?

- permitir a transferência de quadros da origem para o destino
- identificar, de forma exclusiva, um nó em uma rede

#### 6 - Consulte a figura. PC1 emite uma solicitação ARP porque ele precisa enviar um pacote para PC2. Nesse cenário, o que acontecerá a seguir?

![[Pasted image 20240612090706.png]]

- O PC2 enviará uma resposta ARP com o endereço MAC do PC2.

#### 7 - Que endereços são mapeados pelo ARP?

- Endereço IPv4 para um endereço MAC de destino

#### 8 - Consulte a figura. Os switches Sw1 e Sw2 têm tabelas de endereços MAC que são preenchidas com todos os endereços MAC dos host exibidos. Se o host H1 enviar um quadro com o endereço de destino FFFF.FFFF.FFFF, qual será o resultado?

![[Pasted image 20240612090751.jpg]]

- Sw1 inundará o quadro em todas as portas, exceto na porta de entrada. O quadro será inundado por Sw2 e processado pelos hosts H2, H3 e H4.

#### 9 - Consulte a figura. O Host A precisa enviar dados para o servidor, mas não sabe o endereço MAC. Quando o host A envia uma solicitação de ARP, que resposta estará na resposta ARP?

![[Pasted image 20240612090810.png]]

- 00:0D:00:B4:12:F3

#### 10 - Quando o PC0 pinga o servidor web, qual endereço MAC é o endereço MAC de origem no quadro de R2 para o servidor web?

![[Pasted image 20240612091653.png]]
  
Quando o PC0 pinga o servidor web, qual endereço MAC é o endereço MAC de origem no quadro de R2 para o servidor web?

- 0001.C972.4202

#### 11 - Que afirmativa descreve uma característica dos endereços MAC?

- Eles são o endereço físico da NIC ou da interface.

#### 12 - Quais são as duas características que descrevem os endereços MAC?

- endereço físico atribuído à NIC
- identifica origem e destino no cabeçalho da Camada 2

