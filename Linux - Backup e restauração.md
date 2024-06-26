Os sistemas Linux oferecem uma variedade de ferramentas de software para backup e restauração de dados. Essas ferramentas são projetadas para serem eficientes e seguras, garantindo a proteção dos dados e, ao mesmo tempo, permitindo-nos acessar facilmente os dados de que precisamos.

Ao fazer backup de dados em um sistema Ubuntu, podemos utilizar ferramentas como:

- Rsync
- Deja Dup
- Duplicity

Rsync é uma ferramenta de código aberto que nos permite fazer backup de arquivos e pastas de forma rápida e segura em um local remoto.
É particularmente útil para transferir grandes quantidades de dados pela rede, pois transmite apenas as partes alteradas de um arquivo.

Duplicity é outra ferramenta gráfica de backup para Ubuntu que fornece aos usuários proteção abrangente de dados e backups seguros.Ele também usa Rsync como back-end e oferece adicionalmente a possibilidade de criptografar cópias de backup e armazená-las em mídias de armazenamento remotas, como servidores FTP, ou serviços de armazenamento em nuvem, como Amazon S3.

Deja Dup é uma ferramenta gráfica de backup para Ubuntu que simplifica o processo de backup, permitindo-nos fazer backup de nossos dados de forma rápida e fácil.
Ele fornece uma interface amigável para criar cópias de backup de dados em mídia de armazenamento local ou remota. Ele usa Rsync como backend e também suporta criptografia de dados.

Alternativamente, podemos criptografar backups em sistemas Ubuntu utilizando ferramentas como GnuPG, eCryptfs e LUKS.

### Instalando o rsync

```bash
sudo apt install rsync -y
```

Para fazer backup de um diretório inteiro usando `rsync`, podemos usar o seguinte comando:

### Rsync - Faça backup de um diretório local para nosso servidor de backup

```bash
rsync -av /path/to/mydirectory user@backup_server:/path/to/backup/directory
```

Este comando copiará todo o diretório (`/path/to/mydirectory`) para um host remoto (`backup_server`), para o diretório `/path/to/backup/directory`. A opção `archive` (`-a`) é usada para preservar os atributos originais do arquivo, como permissões, carimbos e data e hora, etc., o uso da opção `verbose` (`-v`) fornece uma saída detalhada do andamento da operação `rsync`.

Também podemos adicionar opções adicionais para personalizar o processo de backup, como usar compactação e backups incrementais. Podemos fazer isso da seguinte maneira:

```bash
rsync -avz --backup --backup-dir=/path/to/backup/folder --delete /path/to/mydirectory user@backup_server:/path/to/backup/directory
```


Com isso, fazemos backup do arquivo `mydirectory` para o arquivo remoto `backup_serverp`, reservando os atributos, carimbos de data e hora e permissões do arquivo original, e habilitamos a compactação ( `-z` ) para transferências mais rápidas.

A opção `--backup` cria backups incrementais no diretório `/path/to/backup/folder` e `--delete` remove arquivos do host remoto que não estão mais presentes no diretório de origem.

Se quisermos restaurar nosso diretório do servidor de backup para o diretório local, podemos usar o seguinte comando:

### Rsync - Restaure nosso backup

```bash
rsync -av user@remote_host:/path/to/backup/directory /path/to/mydirectory
```

## Rsync criptografado

Ao usar o SSH, podemos criptografar nossos dados à medida que são transferidos, tornando muito mais difícil o acesso a eles por qualquer indivíduo não autorizado.

Além disso, também podemos usar firewalls e outros protocolos de segurança para garantir que nossos dados sejam mantidos seguros e protegidos durante a transferência.

Dizemos para o `rsync` usar SSH da seguinte forma:

### Transferência segura do nosso backup

```bash
rsync -avz -e ssh /path/to/mydirectory user@backup_server:/path/to/backup/directory
```

A própria chave de criptografia também é protegida por um conjunto abrangente de protocolos de segurança, tornando ainda mais difícil para qualquer pessoa não autorizada obter acesso aos dados.

## Sincronização automática

Para ativar a sincronização automática usando `rsync`, você pode usar uma combinação de `cron`e `rsync`para automatizar o processo de sincronização.

Portanto, criamos um novo script chamado `RSYNC_Backup.sh`, que acionará o comando `rsync` para sincronizar nosso diretório local com o remoto.

#### RSYNC_Backup.sh
```bash
#!/bin/bash

rsync -avz -e /path/to/mydirectory user@backup_server:/path/to/backup/directory
```

Então, para garantir que o script seja executado corretamente, devemos fornecer as permissões necessárias. Além disso, também é importante certificar-se de que o script pertence ao usuário correto.

```bash
chmod +x RSYNC_Backup.sh
```

Depois disso, podemos criar um crontab que diz ao `cron` para executar o script a cada hora no minuto 0. Podemos ajustar o tempo para atender às nossas necessidades. Para fazer isso, o crontab precisa do seguinte conteúdo:

### Sincronização automática - Crontab

```bash
0 * * * * /path/to/RSYNC_Backup.sh
```

Com esta configuração, o `cron` será responsável por executar o script no intervalo desejado, garantindo que o comando `rsync` seja executado e o conteúdo do diretório local esteja sincronizado com o host remoto.









































