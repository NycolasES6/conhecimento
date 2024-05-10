#redes #cyber 
# Métodos de criptografia

A criptografia é usada para proteger os dados. Se um invasor capturar dados criptografados, não poderá decifrá-los em um período de tempo razoável.

Os padrões WPA e WPA2 utilizam os seguintes protocolos de criptografia:

- **Temporal Key Integrity Protocol (TKIP) -** TKIP é o método de criptografia usado pelo WPA. Ele fornece suporte para equipamentos WLAN herdados, abordando as falhas exclusivas associadas ao método de criptografia 802.11 WEP. Ele usa o WEP, mas criptográfico é útil para carregar a camada 2 usando o TKIP e executa um MIC (Message Integrity Check) no pacote criptografado para garantir que a mensagem não seja alterada.
- **Advanced Encryption Standard (AES) -** AES é o método de criptografia usado pelo WPA2. É o método preferido porque é um método muito mais forte de criptografia. Ele usa o Modo de Cifra de Contador com o Protocolo de Código de Autenticação de Mensagem em Cadeia de Blocos (CCMP - Chaining Message Authentication Code Protocol) que permite que os hosts de destino reconheçam se os bits criptografados e não criptografados foram alterados.

Na figura, o administrador está configurando o roteador sem fio para usar WPA2 com criptografia AES na faixa de 2,4 GHz.

![[Pasted image 20240510132703.png]]



























