#SO #Windows 
# Processos, Threads e Serviços

Um aplicativo do Windows é composto de processos. O aplicativo pode ter um ou muitos processos dedicados a ele. Um processo é qualquer programa em execução no momento. Cada processo que é executado é composto de pelo menos um thread. Um thread é uma parte do processo que pode ser executado. O processador executa cálculos na thread. Para configurar processos do Windows, procure o Gerenciador de Tarefas. A guia Processos do Gerenciador de Tarefas é mostrada na figura.

![[Pasted image 20240514105042.jpg]]

Todos os threads dedicados a um processo estão contidos no mesmo espaço de endereço. Isso significa que esses threads podem não acessar o espaço de endereço de qualquer outro processo. Isso evita a corrupção de outros processos. Como Windows é multitarefas, vários threads podem ser executados ao mesmo tempo. A quantidade de threads que podem ser executados ao mesmo tempo depende do número de processadores do computador.

Alguns dos processos executados pelo Windows são serviços. Estes são programas que são executados em segundo plano para suportar o sistema operativo e as aplicações. Eles podem ser configurados para iniciar automaticamente quando o Windows for inicializado ou podem ser iniciados manualmente. Eles também podem ser interrompidos, reiniciados ou desativados.

Os serviços fornecem funcionalidade de longa execução, como sem fio ou acesso a um servidor FTP. Para configurar os Serviços do Windows, procure serviços. O miniaplicativo do painel de controle dos Serviços do Windows é mostrado na figura.

![[Pasted image 20240514105242.jpg]]

Tenha muito cuidado ao manipular as configurações desses serviços. Alguns programas dependem de um ou mais serviços para funcionar corretamente. Encerrar um serviço pode afetar negativamente aplicativos ou outros serviços.


