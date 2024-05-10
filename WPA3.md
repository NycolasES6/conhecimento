#cyber #redes 

# WPA3

No momento da redação deste artigo, os dispositivos que suportam autenticação WPA3 não estavam disponíveis. No entanto, o WPA2 não é mais considerado seguro. WPA3, disponível, é o método de autenticação 802.11 recomendado. O WPA3 inclui quatro recursos:

- WPA3-Pessoal (Pessoal)
- WPA3-Enterprise (Corporativo)
- Redes abertas
- Integração da Internet das Coisas (IoT)

- **WPA3-Pessoal (Pessoal)** - No WPA2-Personal, os sensores de ameaças podem ouvir o “aperto de mão” (aperto de mão) entre um cliente sem fio e o AP e usar um ataque de força brutal para tentar adivinhar o PSK. O WPA3-Personal impede esse ataque usando a autenticação simultânea de iguais (SAE), um recurso especificado no IEEE 802.11-2016. O PSK nunca é exposto, tornando-se impossível para o caçador adivinhar.
- **WPA3-Enterprise (Corporativo)** - O WPA3-Enterprise ainda usa autenticação 802.1X/EAP. No entanto, é necessário o uso de um conjunto criptográfico de 192 bits e eliminar a mistura de protocolos de segurança para os padrões 802.11 anteriores. O WPA3-Enterprise adere ao conjunto comercial de algoritmos de segurança nacional (CNSA - Commercial National Security Algorithm), que é comumente usado em redes Wi-Fi de alta segurança.
- **Redes abertas** - As redes abertas no WPA2 enviam o tráfego do usuário em texto não autenticado e limpo. No WPA3, as redes Wi-Fi abertas ou públicas ainda não usam autenticação. No entanto, eles usam o OWE (Opportunistic Wireless Encryption) para criptografar todo o tráfego sem fio.
- **Integração da IoT** - Embora o WPA2 tenha incluído o Wi-Fi Protected Setup (WPS) para dispositivos embarcados rapidamente, sem configurá-los primeiro, o WPS é vulnerável a uma variedade de ataques e não é recomendado. Além disso, os dispositivos de IoT são tipicamente decapitados, o que significa que eles não têm GUI interna para configuração e precisam de qualquer maneira fácil de se conectar à rede sem fio. O Protocolo de provisionamento de dispositivo (DPP - Device Provisioning Protocol) foi projetado para atender a essa necessidade. Cada dispositivo projetado para operar sem tela, teclado e mouse possui uma chave pública codificada diretamente no seu firmware ou hardware. A chave é tipicamente impressa na parte externa do dispositivo ou em sua embalagem como um código de resposta rápida (QR Code). O administrador da rede pode digitalizar o código QR e integrar rapidamente o dispositivo. Embora não faça parte do padrão WPA3, o DPP substituirá o WPS ao longo do tempo.
















