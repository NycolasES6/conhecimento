#SO 
# Integridade da inicialização

Os invasores podem atacar a qualquer momento, mesmo no curto espaço de tempo que um sistema leva para iniciar. É fundamental garantir que os sistemas e dispositivos permaneçam seguros durante a inicialização.

## O que é integridade de inicialização

A integridade de inicialização garante que o sistema seja confiável e não tenha sido alterado enquanto o sistema operacional é carregado.

O firmware - instruções de software sobre as funções básicas do computador - é armazenado em um pequeno chip de memória na placa-mãe. O sistema básico de entrada / saída (BIOS) é o primeiro programa executado quando você liga o computador. 

A Unified Extensible Firmware Interface (UEFI), uma versão mais recente do BIOS, define uma interface padrão entre o sistema operacional, o firmware e os dispositivos externos. Um sistema que usa UEFI é preferível a um que usa BIOS porque um sistema UEFI pode ser executado no modo de 64 bits.

## Como funciona a inicialização segura

A inicialização segura é um padrão de segurança para garantir que um dispositivo inicialize usando software confiável. Quando um sistema de computador é inicializado, o firmware verifica a assinatura de cada parte do software de inicialização, incluindo os drivers de firmware UEFI, aplicativos UEFI e o sistema operacional. Se as assinaturas forem válidas, o sistema inicializará e o firmware dará controle ao sistema operacional.

## O que é a inicialização medida ?

A inicialização medida fornece uma validação mais forte do que a inicialização segura. A inicialização medida mede cada componente, começando pelo firmware até os drivers de inicialização, e armazena as medidas no chip TMP para criar um log. O log pode ser testado remotamente para verificar o estado de inicialização do cliente. A inicialização medida pode identificar aplicativos não confiáveis que tentam carregar e também permite que o antimalware seja carregado mais cedo.















