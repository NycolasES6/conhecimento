#redes #CISCO

# Configurações de redes sem fio

A interface de Configurações sem fio básicas do Packet Tracer é mostrada na figura. Os roteadores sem fio que usam os padrões 802.11 têm várias configurações que devem ser ajustadas. Estas configurações incluem:

- **Modo de rede** - Determina o tipo de tecnologia que deve ser suportada. Por exemplo,**802.11b**, **802.11g**,**802.11n** ou **Mixed Mode (Modo misto).**
- **Nome de rede** - Usada para identificar a WLAN. Todos os dispositivos que desejam participar na WLAN devem ter o mesmo SSID.
- **Canal padrão** - Especifica o canal no qual a comunicação ocorrerá. Por padrão, é configurado para **Automático** para permitir que o ponto de acesso (AP) determine o melhor canal a usar.
- **Broadcast de SSID** - Determina se o SSID será transmitido para todos os dispositivos dentro do intervalo. Por padrão, é configurado para **Ativado**.

![[Pasted image 20240520082032.png]]

**Modo de rede**

O protocolo 802.11 pode fornecer melhor taxa de trasnferência, dependendo do ambiente de rede sem fio. Se todos os dispositivos sem fio se conectarem com o mesmo padrão 802.11, poderão ser obtidas as velocidades máximas desse padrão. Se o ponto de acesso estiver configurado para aceitar apenas um padrão 802.11, os dispositivos que não usarem esse padrão não poderão se conectar ao access point.

Um ambiente de rede sem fio com modo misto pode incluir dispositivos que utilizem qualquer padrão Wi-Fi atual. Esse ambiente oferece acesso fácil para dispositivos antigos que precisam de uma conexão sem fio, mas não são compatíveis com os padrões mais recentes.

Ao criar uma rede sem fio, é importante que os componentes sem fio se conectem à WLAN apropriada. Isso é feito por meio do SSID.

O SSID é uma string alfanumérica que diferencia maiúsculas e minúsculas até 32 caracteres. Ele é enviado no cabeçalho de todos os quadros transmitidos pela WLAN. O SSID serve para informar a dispositivos sem fio, chamados estações sem fio (STA), qual WLAN eles pertencem e com quais outros dispositivos eles podem se comunicar.

Usamos o SSID para identificar uma rede sem fio específica É basicamente o nome da rede. Roteadores sem fio usualmente transmitem seu SSIDs configurados por default O broadcast SSID permite que outros dispositivos e clientes sem fio detectem automaticamente o nome da rede sem fio. Se o broadcast SSID estiver desativado, insira manualmente o SSID nos dispositivos sem fio.

A desativação do broadcast SSID pode dificultar a detecção da rede sem fio para clientes legítimos. Entretanto, simplesmente desativar o broadcast SSID não é suficiente para evitar que clientes não autorizados se conectem à rede sem fio. Todas as redes sem fio devem usar a criptografia mais forte disponível para restringir o acesso não autorizado.











