#linux #comandos 

# Análise de logs

```sh
wc -l access.log
```

Mostra quantas linhas tem o arquivo

```sh
cat access.log | cut -d " " -f 1
```

```sh
cat access.log | cut -d " " -f 1 | sort -u
```

O **sort -u** vai remover os itens duplicados

```sh
cat access.log | cut -d " " -f 1 | sort | uniq -c
```

O **uniq -c** conta quantas vezes cada linha repetiu

```sh
cat access.log | cut -d " " -f 1 | sort | uniq -c | sort -un
```

O **sort -un** vai listar em ordem numérica, se adicionarmos o **r**, lista de forma numérica de forma reversa

















