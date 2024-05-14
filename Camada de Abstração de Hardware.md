#SO #Windows 

# Camada de Abstração de Hardware

Computadores Windows usam muitos tipos diferentes de hardware. O sistema operacional pode ser instalado em um computador comprado ou em um computador que é montado pelo usuário. Quando o sistema operacional está instalado, ele deve ser isolado das diferenças no hardware. A arquitetura básica do Windows é mostrada na figura.

![[Pasted image 20240514100133.png]]

Uma camada de abstração de hardware (HAL) é um software que lida com toda a comunicação entre o hardware e o kernel. O kernel é o núcleo do sistema operacional e tem controle sobre todo o computador. Ele lida com todas as solicitações de entrada e saída, memória e todos os periféricos conectados ao computador.

Em alguns casos, o kernel ainda se comunica diretamente com o hardware, portanto não é completamente independente do HAL. O HAL também precisa do kernel para executar algumas funções.













