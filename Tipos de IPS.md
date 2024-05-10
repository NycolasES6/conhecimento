#redes #cyber
# Tipos de IPS

Existem dois tipos principais de IPS disponíveis: IPS baseado em host e IPS baseado em rede.

**IPS de host**

O IPS baseado em host (HIPS) é um software instalado em um host para monitorar e analisar atividades suspeitas. Uma vantagem significativa do HIPS é que ele pode monitorar e proteger o sistema operacional e os processos críticos do sistema que são específicos para esse host. Com conhecimento detalhado do sistema operacional, o HIPS pode monitorar atividades anormais e impedir que o host execute comandos que não correspondam ao comportamento típico. Esse comportamento suspeito ou mal-intencionado pode incluir atualizações de registro não autorizadas, alterações no diretório do sistema, execução de programas de instalação e atividades que causam estouros de buffer. O tráfego de rede também pode ser monitorado para impedir que o host participe de um ataque de negação de serviço (DoS) ou faça parte de uma sessão de FTP ilícita.

HIPS pode ser pensado como uma combinação de software antivírus, software antimalware e um firewall. Combinado com um IPS baseado em rede, o HIPS é uma ferramenta eficaz para fornecer proteção adicional para o host.

Uma desvantagem do HIPS é que ele opera apenas a nível local. Ele não tem uma visão completa da rede ou eventos coordenados que possam estar acontecendo em toda a rede. Para ser eficaz em uma rede, o HIPS deve ser instalado em cada host e ter suporte para cada sistema operacional.

### Vantagens

- Fornece proteção específica para um sistema operacional host
- Fornece proteção em nível de aplicativo e sistema operacional
- Protege o host depois que a mensagem é descriptografada

### Desvantagens

- Dependente do sistema operacional
- Deve ser instalado em todos os hosts

---

**IPS baseado em rede**

Um IPS baseado em rede pode ser implementado usando um dispositivo IPS dedicado ou não dedicado. As implementações de IPS baseadas em rede são um componente crítico da prevenção de intrusões. Existem soluções IDS/IPS baseadas em host, mas elas devem ser integradas a uma implementação IPS baseada em rede para garantir uma arquitetura de segurança robusta.

Os sensores detectam atividades maliciosas e não autorizadas em tempo real e podem agir quando necessário. Como mostrado na figura, os sensores são implantados em pontos de rede designados. Isso permite que os gerentes de segurança monitorem a atividade da rede enquanto ela estiver ocorrendo, independentemente do local do alvo de ataque.

**Exemplo de implantação do sensor IPS**

![[Pasted image 20240510184631.png]]




