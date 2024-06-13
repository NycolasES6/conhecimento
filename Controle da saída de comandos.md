#Linux 
# Controle da saída de comandos

A conhecida frase "no Linux, tudo é um arquivo" descreve a arquitetura do sistema operacional. Tudo no sistema, de processos a arquivos e diretórios, é representado por um `file descriptor` que é abstraído sobre a camada do sistema de arquivos virtual no kernel. Esse design oferece uma interface uniforme para aplicativos e usuários. O Linux inclui muitas técnicas para processar descritores de arquivo em arquivos voltados para o usuário.

Uma dessas técnicas é o redirecionamento de entrada e saída. Quando você abre um terminal, o sistema recebe entradas do teclado e envia a saída e os erros do programa para a tela. A entrega da saída usa três fluxos de entrada/saída (E/S) distintos chamados _entrada padrão_, _saída padrão_ e _erro padrão_ no Linux. Esses fluxos são abertos para todos os programas quando estes são iniciados.

O canal da _entrada padrão_, ou `stdin`, é onde um programa lê a entrada dele. A saída de texto normal é transmitida pela _saída padrão_, ou `stdout`. As mensagens de erro que um programa pode produzir são enviadas por _erro padrão_, ou `stderr`.

Esses canais representam fluxos de dados entre o terminal, programas e arquivos. Você tem controle total sobre como esses dados fluem. O shell oferece mecanismos para redirecionar fluxos quando um comando é executado. Como resultado, o shell pode ler um arquivo em vez de receber entradas interativas do usuário, ou o programa pode descartar mensagens de erro que você considera inúteis.