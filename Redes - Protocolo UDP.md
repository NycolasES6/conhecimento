#redes 

# Redes - Protocolo UDP

O protocolo UDP assim como o TCP é um protocolo de transporte de dados, no entanto, ele não é confiável pois não garante a entrega dos dados.

O protocolo UDP não é orientado a conexão, ou seja, não é necessário estabelecer uma conexão antes de começar a transmitir

Sendo assim ele é um protocolo de entrega muito mais rápido e amplamente usado em streaming de vídeo, áudio, e comunicações onde o foco é a velocidade.

## Cabeçalho

![[Pasted image 20240618111802.png]]

UDP é comumente usado por DNS, DHCP, TFTP, NFS e SNMP. Também é usado com aplicações em tempo real, como streaming de mídia ou VoIP. UDP é um protocolo de camada de transporte não orientado à conexão. Ele tem uma sobrecarga muito mais baixa que o TCP, porque não é orientado a conexão e não oferece retransmissão, sequenciamento e mecanismos de controle de fluxo sofisticados que fornecem confiabilidade. A estrutura de segmentos UDP, mostrada na figura, é muito menor que a estrutura de segmentos da TCP.

**Nota:** UDP realmente divide dados em datagramas. No entanto, o termo genérico “segmento” é comumente usado

![[Pasted image 20240507134601.png]]

Embora UDP seja normalmente chamado de não confiável, em contraste com a confiabilidade do TCP, isso não significa que os aplicativos que usam UDP são sempre não confiáveis, nem significa que o UDP é um protocolo inferior. Isso simplesmente significa que essas funções não são fornecidas pelo protocolo da camada de transporte e devem ser implementadas em outros locais, se houver necessidade.

A baixa sobrecarga do UDP o torna muito interessante para protocolos que efetuam transações simples de requisição e resposta. Por exemplo, usar TCP para o DHCP geraria tráfego de rede desnecessário. Se nenhuma resposta for recebida, o dispositivo reenvia a solicitação.


























