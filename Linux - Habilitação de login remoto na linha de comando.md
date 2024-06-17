#Linux 
# Linux - Habilitação de login remoto na linha de comando

Na linha de comando, você habilita o login remoto por SSH usando o comando `systemctl`. O comando `systemctl` controla os serviços do sistema, como o serviço SSH. Use o comando `systemctl` com o subcomando `enable` para habilitar um serviço, juntamente com a opção `--now` para tornar a alteração imediata, seguida pelo nome do serviço que você deseja iniciar.

![[Pasted image 20240617135455.png]]

Verifique se um serviço está ativo usando o comando `systemctl is-active` seguido pelo nome do serviço. Você pode usar o comando `systemctl is-active` sem um privilégio sudo porque esse comando não modifica o serviço.

![[Pasted image 20240617135556.png]]

Verifique se um serviço está ativo e obtenha outras informações usando o comando `systemctl status` seguido pelo nome do serviço.

![[Pasted image 20240617135618.png]]

## Transferência de arquivos a partir da linha de comando

O comando `scp` copia um arquivo de um computador para outro por meio de uma conexão de rede criptografada. O comando `scp` exige dois argumentos, na seguinte ordem: os arquivos a serem movidos e o local de destino.

Para copiar um arquivo local para um servidor remoto, forneça o caminho para o arquivo que deseja copiar e o servidor e o diretório de destino. Semelhante ao comando `ssh`, o comando `scp` exige uma senha para autenticar o usuário.

![[Pasted image 20240617140327.png]]

Você também pode copiar um arquivo de um sistema remoto para o computador local.

![[Pasted image 20240617140344.png]]

Você também pode copiar um arquivo de um host remoto para outro host remoto.

![[Pasted image 20240617140419.png]]



















