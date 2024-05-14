#SO #Windows 
# Alocação e alças de memória

Um computador funciona armazenando instruções na RAM até que a CPU os processe. O espaço de endereço virtual para um processo é o conjunto de endereços virtuais que o processo pode usar. O endereço virtual não é o local físico real na memória, mas uma entrada em uma tabela de página que é usada para traduzir o endereço virtual para o endereço físico.

Cada processo em um computador Windows de 32 bits suporta um espaço de endereço virtual que permite endereçar até 4 gigabytes. Cada processo num computador Windows de 64 bits suporta um espaço de endereço virtual de 8 terabytes.

Cada processo de espaço do usuário é executado em um espaço de endereço privado, separado de outros processos de espaço do usuário. Quando o processo de espaço do usuário precisa acessar recursos do kernel, ele deve usar um identificador de processo. Isso ocorre porque o processo de espaço do usuário não tem permissão para acessar diretamente esses recursos do kernel. O identificador do processo fornece o acesso necessário para o processo de espaço do usuário sem uma conexão direta com ele.

Uma ferramenta poderosa para visualizar a alocação de memória é RAMMap, que é mostrado na figura. RAMMap faz parte do conjunto de ferramentas do Windows Sysinternals. Ele pode ser baixado da Microsoft. RAMMap fornece uma riqueza de informações sobre como o Windows alocou memória do sistema para o kernel, processos, drivers e aplicativos.

![[Pasted image 20240514105801.jpg]]


















