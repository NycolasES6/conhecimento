#redes 

# SNMP

O protocolo SNMP (Protocolo Simples de Gerenciamento de Rede) permite que os administradores gerenciem dispositivos finais como servidores, estações de trabalho, roteadores, switches e dispositivos de segurança em uma rede IP. Permite que os administradores de rede monitorem o desempenho da rede, encontrem e resolvam os problemas da rede e planejem o crescimento da rede.

O SNMP é um protocolo da camada de aplicação que fornece um formato de mensagem para a comunicação entre gerenciadores e agentes.

Como mostrado na figura, o sistema SNMP consiste em dois elementos.

- Gerenciador SNMP que executa o software de gerenciamento SNMP.
- Agentes SNMP que são os nós que estão sendo monitorados e gerenciados.

O Management Information Base (MIB) é um banco de dados dos agentes que armazena dados e estatísticas operacionais sobre o dispositivo.

Para configurar o SNMP em um dispositivo de rede, primeiramente é necessário definir a relação entre o gerenciador e o agente.

O gerenciador de SNMP faz parte de um sistema de gerenciamento de rede (NMS). O gerenciador de SNMP executa o software de gerenciamento de SNMP. Conforme mostrado na figura, o gerente SNMP pode coletar informações de um agente SNMP usando a ação "get" e pode alterar as configurações em um agente usando a ação "set". Além disso, os agentes SNMP podem encaminhar informações diretamente para um gerenciador de rede usando “traps”.

![[Pasted image 20240513104713.png]]























