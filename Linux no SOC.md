#SO #Linux 

# Linux no SOC

A flexibilidade fornecida pelo Linux é um ótimo recurso para o SOC. Todo o sistema operacional pode ser adaptado para se tornar a plataforma de análise de segurança perfeita. Por exemplo, os administradores podem adicionar apenas os pacotes necessários ao sistema operacional, tornando-o simples e eficiente. Ferramentas de software específicas podem ser instaladas e configuradas para funcionar em conjunto, permitindo que os administradores criem um computador personalizado que se encaixe perfeitamente no fluxo de trabalho de um SOC.

A figura mostra o Sguil, que é o console do analista de segurança cibernética em uma versão especial do Linux chamada Security Onion. O Security Onion é um conjunto de ferramentas de código aberto que trabalham juntas para análise de segurança de rede.

![[Pasted image 20240514170459.png]]

### Software de captura de pacotes de rede

- Uma ferramenta crucial para um analista de SOC, pois permite observar e entender cada detalhe de uma transação de rede.
- Wireshark é uma ferramenta popular de captura de pacotes.

### Ferramentas de análise de malware

- Essas ferramentas permitem que os analistas executem e observem com segurança a execução de malware sem o risco de comprometer o sistema subjacente.

### Sistemas de detecção de intrusão (IDSs)

- Essas ferramentas são usadas para monitoramento e inspeção de tráfego em tempo real.
- Se qualquer aspecto do tráfego atualmente em fluxo corresponder a qualquer uma das regras estabelecidas, uma ação predefinida será executada.

### Firewalls

Este software é usado para especificar, com base em regras predefinidas, se o tráfego tem permissão para entrar ou sair de uma rede ou dispositivo.

### Gerenciadores de log

- Os arquivos de log são usados para registrar eventos.
- Como uma rede pode gerar um número muito grande de entradas de log, o software do gerenciador de logs é empregado para facilitar o monitoramento de log.

### Segurança das informações e gerenciamento de eventos (SIEM)

Os SIEMs fornecem análise em tempo real de alertas e entradas de log geradas por dispositivos de rede, como IDSs e firewalls.

### Sistemas de emissão de bilhetes

A atribuição de tíquetes de tarefa, edição e gravação é feita através de um sistema de gerenciamento de tíquetes. Os alertas de segurança são frequentemente atribuídos a analistas por meio de um sistema de emissão de bilhetes.


