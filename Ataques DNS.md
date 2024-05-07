#redes #cyber 

# Ataques DNS

O protocolo DNS (Domain Name Service) define um serviço automatizado que corresponde a nomes de recursos, como www.cisco.com, com o endereço de rede numérico necessário, como o endereço IPv4 ou IPv6. Ele inclui o formato para consultas, respostas e dados e usa os registros de recursos (RR) para identificar o tipo de resposta DNS.

A proteção do DNS geralmente é ignorada. No entanto, é crucial para a operação de uma rede e deve ser protegido adequadamente.

Os ataques de DNS incluem os seguintes:

- Ataques de resolvedor aberto de DNS
- Ataques furtivos de DNS
- Ataques de sombreamento de domínio DNS
- Ataques de tunelamento de DNS

### Ataques de resolvedor aberto de DNS

Muitas organizações usam os serviços de servidores DNS abertos ao público, como o **GoogleDNS** (8.8.8.8), para fornecer respostas às consultas. Esse tipo de servidor DNS é chamado de resolvedor aberto. Um resolvedor aberto de DNS responde a consultas de clientes fora de seu domínio administrativo. Os resolvedores abertos de DNS são vulneráveis a várias atividades maliciosas descritas na tabela.

#### Ataques de envenenamento de cache DNS

Os agentes de ameaças enviam informações de recurso de registro falsificado e falsificado (RR) a um resolvedor de DNS para redirecionar usuários de sites legítimos para sites maliciosos. Os ataques de envenenamento de cache DNS podem ser usados para informar o resolvedor de DNS a usar um servidor de nomes mal-intencionado que fornece informações de RR para atividades mal-intencionadas.

#### Ataques de amplificação e reflexão de DNS

Os agentes de ameaças usam ataques DoS ou DDoS em resolvedores abertos do DNS para aumentar o volume de ataques e ocultar a verdadeira fonte de um ataque. Os agentes de ameaças enviam mensagens DNS para os resolvedores abertos usando o endereço IP de um host de destino. Esses ataques são possíveis porque o resolvedor aberto responderá às perguntas de qualquer pessoa que faça uma pergunta.

#### Ataques de utilização de recursos DNS

Um ataque de DoS que consome os recursos dos resolvedores abertos do DNS. Esse ataque do DoS consome todos os recursos disponíveis para afetar negativamente as operações do resolvedor aberto do DNS. O impacto desse ataque de DoS pode exigir que o resolvedor aberto do DNS seja reinicializado ou que os serviços sejam interrompidos e reiniciados.

### Ataques furtivos de DNS

Para ocultar sua identidade, os agentes de ameaças também usam as técnicas furtivas de DNS descritas na tabela para realizar seus ataques.

#### Fluxo Rápido

Os atores de ameaças usam essa técnica para ocultar seus sites de entrega de phishing e malware atrás de uma rede que muda rapidamente de hosts DNS comprometidos. Os endereços IP do DNS são alterados continuamente em minutos. As redes de bots geralmente empregam técnicas do Fast Flux para impedir a detecção eficaz de servidores mal-intencionados.

#### Fluxo de IP duplo

Os atores de ameaças usam essa técnica para alterar rapidamente o nome do host para os mapeamentos de endereço IP e também para alterar o servidor de nomes autoritativo. Isso aumenta a dificuldade de identificar a fonte do ataque.

#### Algoritmos de geração de domínio

Os atores de ameaças usam essa técnica em malware para gerar aleatoriamente nomes de domínio que podem ser usados como pontos de encontro para seus servidores de comando e controle (C&C).

**Ataques de sombreamento de domínio DNS**

O sombreamento de domínio envolve o agente de ameaças coletando credenciais de conta de domínio para criar silenciosamente vários subdomínios a serem usados durante os ataques. Esses subdomínios normalmente apontam para servidores mal-intencionados sem alertar o proprietário real do domínio pai.
























