#linux #arquivos

O [[linux]] tem várias formas de pesquisar arquivos
# localizando arquivos no linux

### Locate

```sh
$ updatedb
$ locate access.log
```

Primeiro precisamos atualizar a base de dados, e depois que fazemos s busca.

### whereis

```sh
$ whereis nmap
```

Mostra onde fica o [[binário]] do nmap, as configurações e o man

### which

```sh
$ which ping
```

Mostra onde fica o binário do ping

### find 

```sh
$ find /root/ -name desec*
```

Vai procurar dentro do diretório root algum arquivo cujo o nome comece com desec























