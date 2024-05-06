#windows #comandos 

# Dominando o prompt do windows

Semelhante ao prompt do [[linux]], o [[windows]] também é versátil em comandos
## Prompt de comando

```sh
echo %cd%
```

Retorna o diretório atual

```sh
dir
```

Lista os arquivos de uma pasta

```sh
mkdir aluno
```

Cria a pasta aluno

```sh
echo JAN > meses.txt
```

Adiciona JAN em um arquivo meses.txt

```sh
echo FEV  >> meses.txt
```

Adiciona o FEV no final do arquivo meses.txt

```sh
copy meses.txt meses2.txt
```

Copia o arquivo meses para meses2

```sh
del meses.txt
```

Deleta o arquivo meses.txt

```sh
attrib /?
```

Vai mostrar como o comando attrib funciona.

- **/?** : Como se fosse um help 

```sh
attrib +h meses
```

Deixa a pasta meses oculta

```sh
attrib -h meses
```

Deixa a pasta meses visível de novo

```sh
dir /a
```

Lista arquivos e diretórios ocultos

```sh
rmdir meses
```

Apaga a pasta **meses**, (Somente se estiver vazia)

```sh
rmdir /s meses
```

Caso a pasta não estiver vazia, devemos usar o **/s**.

```sh
dir /S desec.txt
```

Procura o arquivo **desec.txt** no sistema

```sh
ipconfig
```

Mostra a sua configuração de [[ip]]

```
ipconfig /all
```

Mostra a sua configuração de [[ip]] de forma mais detalhada

```sh
netstat -n
```

Mostra as conexões de forma numérica

```sh
netstat -p tcp
```

Mostra as conexões tcp

```sh
netstat -p udp
```

Mostra as conexões udp

```sh
tasklist
```

Mostra todas as tarefas em execução no sistema.

```sh
taskkill -pid 6928
```

Mata o processo de pid 6928

```sh
net user
```

Mostra todos os usuários do sistema

```sh
net user Administrator
```

Mostra informações do usuário **Administrator**.

```sh
net user nycolas Admin@123 /add
```

Cria um usuário **nycolas** de senha **Admin@123**.

```sh
net user nycolas /delete
```

Deleta o usuário de nome **nycolas**













