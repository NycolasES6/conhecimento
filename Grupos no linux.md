## Criando grupos

```sh
~ sudo addgroup desenvolvimento

info: Selecting GID from range 1000 to 59999 ...
info: Adding group `desenvolvimento' (GID 1002) ...
```

## Criando usuários

```sh
~ sudo adduser elon

Full Name []:
Room Number []:
Work Phone []:
Home Phone []:
Other []:
Is the information correct? [Y/n] Y
```

### Listar usuários comuns do sistema

```sh
~ sudo awk -F: '$3 >= 1000 {print $1}' /etc/passwd
```

## Adicionando usuários aos grupos

